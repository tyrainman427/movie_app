import requests
import json


def search_film(movie):
    movies_list = []


    url = f"http://www.omdbapi.com/?s={movie}&apikey=5aaeba44"



    response = requests.request("GET", url)

    titles = response.json()
    print(titles)

    # url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/{movie}"
    #
    # headers = {
    #     'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
    #     'x-rapidapi-key': "bff6c04355msh46e32c3afb8d323p1eaeedjsnbf048a37783e"
    #     }
    #
    # response = requests.request("GET", url, headers=headers)
    # titles = response.json()


    with open('film_data.json', 'w') as json_file:
        json.dump(titles, json_file, indent=4, sort_keys=True)


    for i in range(len(titles['Search'])):
        movies_list.append(titles['Search'][i])


    return movies_list

def get_film():
    film_list = []

    movie = ""

    url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{movie}"

    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key': "bff6c04355msh46e32c3afb8d323p1eaeedjsnbf048a37783e"
        }

    response = requests.request("GET", url, headers=headers)
    movie  = response.json().beautiffy()
    return film_list
