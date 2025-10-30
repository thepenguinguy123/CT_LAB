class Movie:
    def __init__(self, title, director, rental_price):
        self.title = title
        self.director = director
        self.rental_price = rental_price
        self.is_rented = False  

class Rental:
    def __init__(self):
        self.movies = []         
        self.total_income = 0.0   

    def add_movie(self, movie):
        self.movies.append(movie)

    def rent_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                if not movie.is_rented:
                    movie.is_rented = True
                    self.total_income += movie.rental_price
                    print(f"You have successfully rented '{movie.title}'.")
                    return
                else:
                    print(f"The movie '{movie.title}' is already rented.")
                    return
        print(f"No movie found with the title '{title}'.")

    def return_movie(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                if movie.is_rented:
                    movie.is_rented = False
                    print(f"You have returned '{movie.title}'.")
                    return
                else:
                    print(f"The movie '{movie.title}' was not rented.")
                    return
        print(f"No movie found with the title '{title}'.")   

    def get_rented_movies(self):
        rented = [movie for movie in self.movies if movie.is_rented]
        if not rented:
            print("No movies are currently rented.")
        else:
            print("Movies currently rented:")
            for movie in rented:
                print(" -", movie.title) 
    
    def get_total_income(self):
        print(f"Total income: ${self.total_income}")

rental_store = Rental()

rental_store.add_movie(Movie("Inception", "Christopher Nolan", 5))
rental_store.add_movie(Movie("Interstellar", "Christopher Nolan", 6))
rental_store.add_movie(Movie("Avatar", "James Cameron", 4))

rental_store.rent_movie("Inception")
rental_store.rent_movie("Avatar")
rental_store.get_rented_movies()
rental_store.return_movie("Avatar")

rental_store.get_total_income()
rental_store.get_rented_movies()