import pandas as pd

df = pd.read_csv('imdb_top_movies.csv')

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace=True)

# Convert Year to integer and Rating to float
df['Year'] = df['Year'].astype(int)
df['Rating'] = df['Rating'].astype(float)

# Check & Remove duplicates
print(f"Number of duplicate rows: {df.duplicated().sum()}")
df.drop_duplicates(inplace=True)

# Clean the Title field to remove numbering
df['Title'] = df['Title'].str.replace(r'^\d+\.\s*', '', regex=True)
df['Title'] = df['Title'].str.strip()

# Save the cleaned dataframe to a new CSV file
df.to_csv('imdb_top_movies_cleaned.csv', index=False)
print("Cleaned data saved to imdb_top_movies_cleaned.csv")

# Display the cleaned dataframe
print(df.head())
