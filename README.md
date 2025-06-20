# Mood-based-Song-Recommender

# Mood-Based Music Recommendation System

## Overview
This system recommends songs based on your current mood using:
- Audio feature analysis
- Natural language processing
- Machine learning recommendations

## Features
- 🎵 32,000+ songs from Spotify
- 😊 7 mood categories
- 🔍 Content-based filtering
- 📊 Interactive visualizations

## Installation
```bash
git clone https://github.com/yourusername/mood-music-recommender.git
cd mood-music-recommender
pip install -r requirements.txt
```

## Usage
Run the main application:
```bash
python app.py
```

Example interaction:
```
How are you feeling today? (or 'quit' to exit): I'm feeling excited and happy!

🎶 Recommended Songs:
Blinding Lights       The Weeknd     happy
Save Your Tears       The Weeknd     happy
good 4 u       Olivia Rodrigo happy
```

## File Structure
```
mood-music-recommender/
├── app.py                  # Main application
├── recommender.py          # Recommendation engine
├── data_processing.py      # Data loading
├── visualization.py        # Visualizations
├── requirements.txt        # Dependencies
└── assets/                 # Visualization images
```

## Data Sources
- [Spotify Songs Dataset](https://github.com/rfordatascience/tidytuesday/tree/master/data/2020/2020-01-21)

## License
MIT
