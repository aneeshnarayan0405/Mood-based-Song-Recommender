import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MinMaxScaler

class MusicRecommender:
    def __init__(self):
        self.features = [
            'danceability', 'energy', 'valence', 'tempo',
            'loudness', 'acousticness', 'instrumentalness'
        ]
        self.scaler = MinMaxScaler()
        self.recommender = None
    
    def load_data(self):
        """Load and preprocess the dataset"""
        url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv"
        df = pd.read_csv(url)
        
        # Data cleaning
        df.columns = df.columns.str.lower()
        df = df.dropna(subset=self.features + ['track_name', 'track_artist'])
        df = df[df['track_artist'] != '']
        
        # Feature scaling
        df[self.features] = self.scaler.fit_transform(df[self.features])
        
        # Mood classification
        conditions = [
            (df['valence'] > 0.7) & (df['energy'] > 0.7),
            (df['valence'] > 0.6) & (df['energy'] > 0.5),
            (df['energy'] > 0.7),
            (df['valence'] < 0.3) & (df['energy'] < 0.4),
            (df['acousticness'] > 0.6),
            (df['instrumentalness'] > 0.7)
        ]
        choices = ['ecstatic', 'happy', 'energetic', 'sad', 'calm', 'instrumental']
        df['mood'] = np.select(conditions, choices, default='neutral')
        
        # Build recommender
        self.recommender = NearestNeighbors(n_neighbors=50, metric='cosine')
        self.recommender.fit(df[self.features])
        
        return df
    
    def detect_mood(self, text):
        """Detect mood from text input"""
        mood_keywords = {
            'ecstatic': ['ecstatic', 'thrilled', 'overjoyed'],
            'happy': ['happy', 'joyful', 'cheerful'],
            'energetic': ['energetic', 'pumped', 'excited'],
            'sad': ['sad', 'depressed', 'melancholy'],
            'calm': ['calm', 'relaxed', 'peaceful'],
            'instrumental': ['instrumental', 'orchestral', 'classical']
        }
        
        text = text.lower()
        for mood, keywords in mood_keywords.items():
            if any(keyword in text for keyword in keywords):
                return mood
        return 'neutral'
    
    def recommend_songs(self, text_input, n=5):
        """Get song recommendations based on mood"""
        mood = self.detect_mood(text_input)
        df = self.load_data()
        mood_tracks = df[df['mood'] == mood]
        
        if len(mood_tracks) == 0:
            return None
        
        # Get diverse recommendations
        seed_indices = np.random.choice(mood_tracks.index, size=min(10, len(mood_tracks)), replace=False)
        _, indices = self.recommender.kneighbors(df.loc[seed_indices, self.features])
        unique_indices = np.unique(indices)
        
        recs = df.loc[unique_indices]
        recs = recs[recs['mood'] == mood]
        return recs[['track_name', 'track_artist', 'mood']].sample(min(n, len(recs)))
