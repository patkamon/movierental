import re
import unittest 
from customer import Customer
from rental import Rental, PriceCode
from movie import Movie, MovieCatalog

class CustomerTest(unittest.TestCase): 
	""" Tests of the Customer class"""
	
	def setUp(self):
		"""Test fixture contains:
		
		c = a customer
		movies = list of some movies
		"""
		self.catalog = MovieCatalog()
		self.c = Customer("Movie Mogul")
		# self.new_movie = Movie("Mulan")
		self.new_movie = self.catalog.get_movie("Mulan")
		self.regular_movie = self.catalog.get_movie("The Arrival")
		self.childrens_movie = self.catalog.get_movie("Jurassic World")


	def test_billing(self):
		"""Test billing is correct."""
		self.assertEqual(15, Rental(self.new_movie, 5, PriceCode.new_release).rental_price())
		self.assertEqual(3, Rental(self.childrens_movie, 4, PriceCode.childrens).rental_price())
		self.assertEqual(3.5, Rental(self.regular_movie, 3, PriceCode.regular).rental_price())

	def test_renter_point(self):
		"""Test renter point work properly."""
		self.assertEqual(5, Rental(self.new_movie, 5, PriceCode.new_release).get_renter_point(5))
		self.assertEqual(1, Rental(self.childrens_movie, 4, PriceCode.childrens).get_renter_point(4))
		self.assertEqual(1, Rental(self.regular_movie, 3, PriceCode.regular).get_renter_point(3))

		# self.assertEqual(5, self.new_movie.get_renter_point(5))
		# self.assertEqual(1, self.childrens_movie.get_renter_point(4))
		# self.assertEqual(1, self.regular_movie.get_renter_point(3))

	def test_statement(self):
		stmt = self.c.statement()
		# visual testing
		print(stmt)
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		self.c.add_rental(Rental(self.new_movie, 4, PriceCode.new_release)) # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])
