import pandas as pd

# 1. Create a "mini-database" of movies for your channel
data = {
    'Movie': ['Send Out', 'Avatar 3', 'M3GAN 2', 'Joker 2', 'Gladiator 2','Send Help 2'],
    'Budget_M': [35, 250, 12, None, 310,10],
    'Genre': ['Thriller', 'Sci-Fi', 'Horror', 'Drama', 'Action','Horror'],
    'Viral_Potential': [9.5, 8.0, 9.8, 7.5, 6.0,9.9]
}

df = pd.DataFrame(data)

# 2. The "Engineer" Filter: Show me only high viral movies with low budgets
# (These are the best for YouTube Automation because they are 'Thirst Traps')
gold_mine = df[(df['Viral_Potential'] > 8.0) & (df['Budget_M'] < 50)]

print("--- ALL MOVIES ---")
print(df)
print("\n--- THE GOLD MINE (Target these for Shorts!) ---")
df['Budget_M'] = df['Budget_M'].fillna(0)
# Sort the Gold Mine by Viral Potential (Highest first)
gold_mine = gold_mine.sort_values(by='Viral_Potential', ascending=False)
# Force the sort and save it
gold_mine = gold_mine.sort_values(by='Viral_Potential', ascending=False)
print(gold_mine)
import matplotlib.pyplot as plt

# Create the Bar Chart: Movie Names vs. Viral Potential
plt.bar(df['Movie'], df['Viral_Potential'], color='skyblue')

# Add the Labels (Engineering 101: Never ship a graph without labels)
plt.xlabel('Movie Title')
plt.ylabel('Viral Potential (0-10)')
plt.title('Cine Trap AI: Content Priority')

# Show the graph
plt.show()
