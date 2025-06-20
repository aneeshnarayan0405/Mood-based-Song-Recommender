from recommender import MusicRecommender
from visualization import show_mood_distribution
import pandas as pd

def main():
    # Initialize recommender
    recommender = MusicRecommender()
    
    # Load data
    df = recommender.load_data()
    
    # Show initial visualization
    show_mood_distribution(df)
    
    # Interactive recommendation interface
    while True:
        user_input = input("\nHow are you feeling today? (or 'quit' to exit): ").strip()
        
        if user_input.lower() == 'quit':
            break
            
        if len(user_input.split()) < 3:
            print("Please enter at least 3 words for better recommendations.")
            continue
            
        try:
            recommendations = recommender.recommend_songs(user_input)
            if recommendations is not None:
                print("\n🎶 Recommended Songs:")
                print(recommendations.to_string(index=False))
            else:
                print("\nNo matching songs found. Try different wording.")
                
        except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()
