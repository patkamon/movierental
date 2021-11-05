import unittest
from customer import Customer
from rental import Rental, PriceCode
from movie import Movie, MovieCatalog


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.catalog = MovieCatalog()
		self.new_movie = self.catalog.get_movie("Mulan")
		self.regular_movie = self.catalog.get_movie("CitizenFour")
		self.childrens_movie = self.catalog.get_movie("Frozen")
		self.k_series = self.catalog.get_movie("Reply 1988")

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = self.catalog.get_movie("CitizenFour")
		rent = Rental(m, 1, PriceCode.for_movie(m))
		self.assertEqual("CitizenFour", m.get_title)
		self.assertEqual(PriceCode.for_movie(m), rent.get_price_code())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1, PriceCode.for_movie(self.new_movie))
		self.assertEqual(rental.rental_price(), 3.0)
		rental = Rental(self.new_movie, 5, PriceCode.for_movie(self.new_movie))
		self.assertEqual(rental.rental_price(), 15.0)
		rental = Rental(self.k_series, 9, PriceCode.for_movie(self.k_series))
		self.assertEqual(rental.rental_price(), 14.0)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 1, PriceCode.for_movie(self.new_movie))
		self.assertEqual(1, rental.get_renter_point(15))
		rental = Rental(self.k_series, 9, PriceCode.for_movie(self.k_series))
		self.assertEqual(1, rental.get_renter_point(10))
