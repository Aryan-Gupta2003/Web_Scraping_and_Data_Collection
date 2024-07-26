import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the cleaned data
df = pd.read_csv('imdb_top_movies_cleaned.csv')

# Histogram Plot the distribution of movie ratings
# plt.figure(figsize=(12, 8))
# sns.histplot(df['Rating'], bins=8, kde=True)
# plt.title('Distribution of Movie Ratings')
# plt.xlabel('Rating')
# plt.ylabel('Frequency')
# plt.show()

# Scatter Plot for Movie Ratings Over the Years
# plt.figure(figsize=(12, 8))
# sns.scatterplot(data=df, x='Year', y='Rating', color='blue', alpha=0.6)
# plt.title('Movie Ratings Over the Years', fontsize=16)
# plt.xlabel('Year', fontsize=14)
# plt.ylabel('Rating', fontsize=14)
# plt.grid(True)
# plt.show()


# Creating Decade column
df['Decade'] = (df['Year'] // 10) * 10  # Create a new 'Decade' column

# Bar Plot the number of movies per year
# plt.figure(figsize=(12, 8))
# sns.countplot(data=df, x='Decade', palette='viridis')
# plt.title('Number of Movies per Decade', fontsize=16)
# plt.xlabel('Decade', fontsize=14)
# plt.ylabel('Number of Movies', fontsize=14)
# plt.xticks(rotation=45, fontsize=10)
# plt.grid(axis='y')
# plt.show()


# Box plot for distribution of ratings across decades
# plt.figure(figsize=(12, 8))
# sns.boxplot(data=df, x='Decade', y='Rating', palette='viridis')
# plt.title('Box Plot of Movie Ratings by Decade')
# plt.xlabel('Decade')
# plt.ylabel('Rating')
# plt.show()

# Pie Chart for Proportion of Movies from different decade
decade_counts = df['Decade'].value_counts()
plt.figure(figsize=(4, 4))
plt.pie(decade_counts, labels=decade_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(decade_counts)))
plt.title('Proportion of Movies by Decade')
plt.show()