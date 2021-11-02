

class Movie:
	"""
	A movie available for rent.
	"""

	def __init__(self, title):#price_code: PriceCode):
		# if not isinstance(price_code, PriceCode):
		# 	raise TypeError("price_code must be in PriceCode")
		# Initialize a new movie. 
		self.title = title
		# self.price_code = price_code

	# def get_price_code(self):
	# 	# get the price code
	# 	return self.price_code
	
	def get_title(self):
		return self.title
	
	def __str__(self):
		return self.title

    # wait for delete
