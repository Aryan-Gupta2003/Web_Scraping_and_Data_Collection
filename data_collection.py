from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import random

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Ensure you have the Chrome WebDriver installed

# URL of the website to scrape
url = "https://www.imdb.com/chart/top"

# Incorporate the Error Handling Mechanism
try:
    driver.get(url)

    # Allow time for the page to load
    time.sleep(5)

    # Extract the relevant information from the HTML code
    movies = []
    rows = driver.find_elements(By.CSS_SELECTOR, 'ul.ipc-metadata-list li')
    for row in rows:
        try:
            title = row.find_element(By.CSS_SELECTOR, 'h3.ipc-title__text').text
            year = row.find_element(By.CSS_SELECTOR, 'span.sc-b189961a-8').text
            rating = row.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--rating').text
            movies.append([title, year, rating])
        except NoSuchElementException as e:
            print(f"Error parsing row: {e}")
            continue

    # Store the information in a pandas dataframe
    df = pd.DataFrame(movies, columns=['Title', 'Year', 'Rating'])
    print(df)

    # Save the dataframe to a CSV file
    df.to_csv('imdb_top_movies.csv', index=False)
    print("Data saved to imdb_top_movies.csv")

except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")

finally:
    # Close the driver
    driver.quit()