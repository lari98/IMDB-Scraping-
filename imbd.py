import requests
from bs4 import BeautifulSoup
import pandas as pd

url_imdb = "https://assets-datascientest.s3.eu-west-1.amazonaws.com/IMDB_en.html"

# Retrieving the HTML code of the page
response = requests.get(url_imdb)
page_imdb = response.content

# Creating a BeautifulSoup object
bs_imdb = BeautifulSoup(page_imdb, 'html.parser')

data = []
# Retrieving HTML code containing all the movie elements
films_imdb = bs_imdb.find('tbody', {'class': 'lister-list'})
rows = films_imdb.find_all('tr') # Retrieving all the rows of the table (each row contains a movie)
# Creating an empty list to store the data
data = [] 

# Looping through each movie element and extracting relevant information
for flims in rows:
    movie_title = flims.find('td', class_='titleColumn') # Retrieving the HTML code containing the title of the movie
    title = movie_title.find('a').get_text() # Retrieving the title of the movie
    release_year = movie_title.find('span', class_='secondaryInfo').get_text() # Retrieving the release year of the movie
    rating= flims.find('td',class_='ratingColumn imdbRating').get_text().replace('\n', '') # Retrieving the rating of the movie and removing the \n character
    film_data = [title, release_year, rating] # Creating a list containing the data of the movie
    data.append(film_data) # Adding the movie data to the list containing all the movies data

# Print rows of data
for i in data:
    print(i)