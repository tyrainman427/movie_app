import requests

def get_film(movie):
    # movie = input("Pick a movie: ")
    url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/blow"

    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key': "bff6c04355msh46e32c3afb8d323p1eaeedjsnbf048a37783e"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)


def search_film():
    film_list = []
    image_list = []

    url = f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/blow"

    headers = {
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
        'x-rapidapi-key': "bff6c04355msh46e32c3afb8d323p1eaeedjsnbf048a37783e"
        }

    response = requests.request("GET", url, headers=headers)

    movie = response.json()

    title = movie.values()

    for n in title:
        print("Title: ",n[0]['title'][0:])
        title = film_list.append(n[0]['title'][0:])


        for item in n[0:]:
            print("Image: ",item['image'])
            image = item['image']
            # return image
    import sqlite3

    conn = sqlite3.connect('film_db.sqlite')
    cur = conn.cursor()
    cur.execute('CREATE TABLE film (title VARCHAR, image VARCHAR)')
    cur.execute('INSERT INTO film (title, image) values (film_list[0], image_list[0])')

    conn.commit()

    conn.close()

search_film()
# string = input("Enter a movie: ")
# search_film(string)
