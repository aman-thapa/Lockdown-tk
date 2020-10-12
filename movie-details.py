import imdb


def detail(movie_name):
    moviesdb = imdb.IMDb()
    try:
        movies = moviesdb.search_movie(movie_name)
        if movies:
            id = movies[0].getID()
            movie = moviesdb.get_movie(id)
            title = movie['title']
            year = movie['year']
            rating = movie['rating']
            directors = movie['directors']
            casting = movie['cast']

            print('Movie Info: ')
            print(f"{title} - {year}")
            print(f"rating: {rating}")
            director = ",".join(map(str, directors))
            print(f"directors: {director}")
            actors = ",".join(map(str, casting[0:5]))
            print(f"actors: {actors}")

    except Exception as error:
        print(error, type(error))


movie_name = input("Enter Movie Name: ")
detail(movie_name)
