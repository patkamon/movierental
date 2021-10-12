import re
import unittest 
from customer import Customer
from rental import Rental
from movie import Movie

class CustomerTest(unittest.TestCase): 
	""" Tests of the Customer class"""
	
	def setUp(self):
		"""Test fixture contains:
		
		c = a customer
		movies = list of some movies
		"""
		self.c = Customer("Movie Mogul")
		self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
		self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
		self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)
		

	def test_billing(self):
		"""Test billing is correct."""
		rent_new_movie = Rental(self.new_movie,5)
		rent_children_movie = Rental(self.childrens_movie, 4)
		rent_regular_movie = Rental(self.regular_movie, 3)

		self.assertEqual(15,rent_new_movie.rental_price())
		self.assertEqual(3, rent_children_movie.rental_price())
		self.assertEqual(3.5, rent_regular_movie.rental_price())

		self.assertEqual(5, rent_new_movie.renter_point())
		self.assertEqual(1, rent_regular_movie.renter_point())
		self.assertEqual(1, rent_children_movie.renter_point())
	
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
		self.c.add_rental(Rental(self.new_movie, 4)) # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])
