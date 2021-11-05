# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental, PriceCode
from customer import Customer


def make_movies():
    movies = [
        catalog.get_movie("The Irishman"),
        catalog.get_movie("CitizenFour"),
        catalog.get_movie("Frozen"),
        catalog.get_movie("El Camino"),
        catalog.get_movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    catalog = MovieCatalog()
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days, PriceCode.for_movie(movie)))
        days += 1
    print(customer.statement())
