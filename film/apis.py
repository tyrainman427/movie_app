import requests
import sqlite3

def get_film():
    film_list = {}
    url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/tt0221027"

    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key': "bff6c04355msh46e32c3afb8d323p1eaeedjsnbf048a37783e"
        }

    response = requests.request("GET", url, headers=headers)

    movie  = response.json()


    i = movie['id']
    # print(movie['year'])
    # print(movie['length'])
    # print(movie['rating'])
    # print(movie['rating_votes'])
    # print(movie['poster'])
    # print(movie['plot'])
    # print(movie['trailer']['link'])
    # print(movie['cast']) # Loop thru this

    return film_list

def search_film(movie):
    movies_list = []

    url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/{movie}"

    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key': "bff6c04355msh46e32c3afb8d323p1eaeedjsnbf048a37783e"
        }

    response = requests.request("GET", url, headers=headers)
    titles = response.json()

    for i in range(len(titles['titles'])):
        movies_list.append(titles['titles'][i])
    return movies_list
