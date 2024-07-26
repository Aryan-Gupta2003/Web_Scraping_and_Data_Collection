import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the cleaned data
df = pd.read_csv('imdb_top_movies_cleaned.csv')

# Creating Decade column
df['Decade'] = (df['Year'] // 10) * 10  # Create a new 'Decade' column

# Sidebar options
st.sidebar.title("Filter Options")
decades = sorted(df['Decade'].unique())
selected_decade = st.sidebar.multiselect("Select Decade(s)", decades, default=decades)

# Filter data based on sidebar selection
filtered_df = df[df['Decade'].isin(selected_decade)]

# Main title
st.title('IMDb Top 250 Movies Analysis')

# Create a grid layout using columns
col1, col2 = st.columns(2)

# Histogram of movie ratings
with col1:
    st.subheader('Distribution of Movie Ratings')
    fig, ax = plt.subplots(figsize=(5, 4))  # Adjust the figure size here
    sns.histplot(filtered_df['Rating'], bins=8, kde=True, ax=ax)
    ax.set_title('Distribution of Movie Ratings')
    ax.set_xlabel('Rating')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

# Scatter plot of movie ratings over the years
with col2:
    st.subheader('Movie Ratings Over the Years')
    fig, ax = plt.subplots(figsize=(5, 4))  # Adjust the figure size here
    sns.scatterplot(data=filtered_df, x='Year', y='Rating', color='blue', alpha=0.6, ax=ax)
    ax.set_title('Movie Ratings Over the Years', fontsize=12)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Rating', fontsize=10)
    ax.grid(True)
    st.pyplot(fig)

# Bar plot of the number of movies per decade
with col1:
       st.subheader('Number of Movies per Decade')
       fig, ax = plt.subplots(figsize=(5, 4))  # Adjust the figure size here
       sns.countplot(data=filtered_df, x='Decade', hue='Decade', palette='viridis', legend=False, ax=ax)
       ax.set_title('Number of Movies per Decade', fontsize=12)
       ax.set_xlabel('Decade', fontsize=10)
       ax.set_ylabel('Number of Movies', fontsize=10)
       ax.tick_params(axis='x', rotation=45, labelsize=10)
       ax.grid(axis='y')
       st.pyplot(fig)

# Box plot for distribution of ratings across decades
with col2:
       st.subheader('Box Plot of Movie Ratings by Decade')
       fig, ax = plt.subplots(figsize=(5, 4))  # Adjust the figure size here
       sns.boxplot(data=filtered_df, x='Decade', y='Rating', hue='Decade', palette='viridis', legend=False, ax=ax)
       ax.set_title('Box Plot of Movie Ratings by Decade', fontsize=12)
       ax.set_xlabel('Decade', fontsize=10)
       ax.set_ylabel('Rating', fontsize=10)
       st.pyplot(fig)

# Pie chart for proportion of movies from different decades
with col1:
       st.subheader('Proportion of Movies by Decade')
       fig, ax = plt.subplots(figsize=(5, 4))  # Adjust the figure size here
       decade_counts = filtered_df['Decade'].value_counts()
       ax.pie(decade_counts, labels=decade_counts.index, autopct='%1.1f%%', startangle=140,
              colors=sns.color_palette('viridis', len(decade_counts)), radius=0.6, textprops=dict(color="black", fontsize=6))
       ax.set_title('Proportion of Movies by Decade', fontsize=12)
       st.pyplot(fig)