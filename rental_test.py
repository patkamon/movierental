import unittest
from customer import Customer
from rental import Rental, PriceCode
from movie import Movie


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan")
		self.regular_movie = Movie("CitizenFour")
		self.childrens_movie = Movie("Frozen")
		self.k_series = Movie("Reply 1988")

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour")
		rent = Rental(m, 1, PriceCode.regular)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.regular, rent.get_price_code())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1, PriceCode.new_release)
		self.assertEqual(rental.rental_price(), 3.0)
		rental = Rental(self.new_movie, 5, PriceCode.new_release)
		self.assertEqual(rental.rental_price(), 15.0)
		rental = Rental(self.k_series, 9, PriceCode.korea_series)
		self.assertEqual(rental.rental_price(), 14.0)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 1, PriceCode.new_release)
		self.assertEqual(15, rental.get_renter_point(15))
		rental = Rental(self.k_series, 9, PriceCode.korea_series)
		self.assertEqual(5, rental.get_renter_point(10))
