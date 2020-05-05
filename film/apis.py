import requests
import json

def get_film():
    film_list = []

    # f = open("film_data.json", "r")
    with open("film_data.json") as f:
        data = json.load(f)

        for item in data:
            print("ID: ", item['id'])



    movie = ""


    url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{movie}"

    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key': "bff6c04355msh46e32c3afb8d323p1eaeedjsnbf048a37783e"
        }

    response = requests.request("GET", url, headers=headers)

    movie  = response.json()

    return film_list

    # print(movie['year'])
    # print(movie['length'])
    # print(movie['rating'])
    # print(movie['rating_votes'])
    # print(movie['poster'])
    # print(movie['plot'])
    # print(movie['trailer']['link'])
    # print(movie['cast']) # Loop thru this



def search_film(movie):
    movies_list = []

    url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/{movie}"

    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key': "bff6c04355msh46e32c3afb8d323p1eaeedjsnbf048a37783e"
        }

    response = requests.request("GET", url, headers=headers)
    titles = response.json()

    # f = open("film_data.json", "w")
    # for i in range(len(titles['titles'])):
    #     f.write(f"{titles['titles'][i]}")
    # print("File saved")
    # f.close()

    for i in range(len(titles['titles'])):
        movies_list.append(titles['titles'][i])
        for x in movies_list:
            with open('film_data.json', 'w') as json_file:
                json.dump(x, json_file)


    return movies_list



# write_file = '/Users/rainman/Desktop/scratch/python/django_project/staticfiles'
#  with open(write_file,’w’, newline = ‘’) as f:
#    writer = csv.writer(f, lineterminator = ‘\n’)
#    writer.writerows(movies_list)
