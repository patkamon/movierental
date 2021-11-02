from rental import Rental, PriceCode
from movie import Movie


class Customer:
    """
       A customer who rents movies.
       The customer object holds information about the
       movies rented for the current billing period,
       and can print a statement of his rentals.
    """
    def __init__(self, name: str):
        """ Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        if rental not in self.rentals:
            self.rentals.append(rental)
    
    def get_name(self):
        return self.name

    def compute_rental_point(self):
        total_point = 0
        for rent in self.rentals:
            total_point += rent.get_renter_point(rent.days_rented)
        return total_point

    def compute_total_charge(self):
        total_charge = 0
        for rent in self.rentals:
            total_charge += rent.rental_price()
        return total_charge


    def statement(self):
        """
            Print all the rentals in current period,
            along with total charges and reward points.
            Returns:
                the statement as a String
        """
        statement = f"Rental Report for {self.name}\n\n"
        fmt = "{:32s}    {:4s} {:6s}\n"
        statement += fmt.format("Movie Title", "Days", "Price")
        fmt = "{:32s}   {:4d} {:6.2f}\n"

        for rental in self.rentals:
            #  add detail line to statement
            statement += fmt.format(rental.get_title(),
                                    rental.get_days_rented(),
                                    rental.rental_price())

        # footer: summary of charges
        statement += "\n"
        statement += "{:32s} {:6s} {:6.2f}\n".format(
                       "Total Charges", "", self.compute_total_charge())
        statement += "Frequent Renter Points earned: {}\n"\
            .format(self.compute_rental_point())

        return statement


if __name__ == "__main__":
    customer = Customer("Edward Snowden")
    print(customer.statement())
    movie = Movie("Hacker Noon", PriceCode.regular)
    customer.add_rental(Rental(movie, 2))
    movie = Movie("CitizenFour", PriceCode.new_release)
    customer.add_rental(Rental(movie, 3))
    print(customer.statement())
