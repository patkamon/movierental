import unittest
from customer import Customer
from rental import Rental
from movie import Movie, PriceCode


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.new_release )
		self.regular_movie = Movie("CitizenFour", PriceCode.regular)
		self.childrens_movie = Movie("Frozen", PriceCode.childrens)
		self.k_series = Movie("Reply 1988", PriceCode.korea_series)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", PriceCode.regular)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.regular, m.get_price_code())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.rental_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.rental_price(), 15.0)
		rental = Rental(self.k_series, 9)
		self.assertEqual(rental.rental_price(), 14.0)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(15, rental.get_renter_point(15))
		rental = Rental(self.k_series, 9)
		self.assertEqual(5, rental.get_renter_point(10))
