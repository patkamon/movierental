from enum import Enum

class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""

    new_release = { "price": lambda days: 3.0*days,
                    "frp": lambda days: days
                  }
    regular = { "price": lambda days: 2+(1.5*(days-2)) if days>2 else 2,
               "frp": lambda days: 1
             }
    childrens = { "price": lambda days: 1.5+(1.5*(days-3)) if days>3 else 1.5,
               "frp": lambda days: 1
             }
    korea_series = {"price": lambda days: 10 + (2 * (days - 7)) if days > 7 else 10,
                 "frp": lambda days: 5
                 }

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days."""
        pricing = self.value["price"]    # the enum member's price formula
        return pricing(days)

    def frequent_point(self, days: int) -> float:
        """Return the rental price for a given number of days."""
        point = self.value["frp"]    # the enum member's price formula
        return point(days)


class Movie:
	"""
	A movie available for rent.
	"""

	def __init__(self, title, price_code: PriceCode):
		def __init__(self, price_code: PriceCode):
			if not isinstance(price_code, PriceCode):
				raise TypeError("price_code must be in PriceCode")
		# Initialize a new movie. 
		self.title = title
		self.price_code = price_code

	def get_price_code(self):
		# get the price code
		return self.price_code
	
	def get_title(self):
		return self.title
	
	def __str__(self):
		return self.title

	def get_renter_point(self, days):
		return self.price_code.frequent_point(days)