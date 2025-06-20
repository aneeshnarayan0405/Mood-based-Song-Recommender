import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def load_and_preprocess_data():
    """Load and preprocess the Spotify dataset"""
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv"
    df = pd.read_csv(url)
    
    # Standardize column names
    df.columns = df.columns.str.lower()
    
    # Define features
    features = [
        'danceability', 'energy', 'valence', 'tempo',
        'loudness', 'acousticness', 'instrumentalness'
    ]
    
    # Clean data
    df = df.dropna(subset=features + ['track_name', 'track_artist'])
    df = df[df['track_artist'] != '']
    
    # Normalize features
    scaler = MinMaxScaler()
    df[features] = scaler.fit_transform(df[features])
    
    return df, features, scaler
