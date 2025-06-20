import matplotlib.pyplot as plt
import seaborn as sns

def show_mood_distribution(df):
    """Show pie chart of mood distribution"""
    mood_counts = df['mood'].value_counts()
    plt.figure(figsize=(10,6))
    plt.pie(mood_counts, labels=mood_counts.index, autopct='%1.1f%%',
            colors=['#FF9999','#66B2FF','#99FF99','#FFCC99','#DAB3FF','#FFB3E6'])
    plt.title('Distribution of Moods in Dataset')
    plt.savefig('assets/mood_distribution.png')
    plt.show()

def show_feature_plot(df):
    """Show feature relationships"""
    plt.figure(figsize=(12,6))
    sns.scatterplot(data=df, x='tempo', y='valence', hue='mood',
                   palette='viridis', alpha=0.6, s=100)
    plt.title('Mood Distribution by Tempo and Valence')
    plt.xlabel('Tempo (BPM)')
    plt.ylabel('Valence (Positivity)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('assets/feature_plot.png')
    plt.show()
