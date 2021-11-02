# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental, PriceCode
from customer import Customer


def make_movies():
    movies = [
        Movie("The Irishman"),
        Movie("CitizenFour"),
        Movie("Frozen"),
        Movie("El Camino"),
        Movie("Particle Fever")
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days, PriceCode.regular))
        days += 1
    print(customer.statement())
