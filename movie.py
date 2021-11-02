
class Movie:
    """
    A movie available for rent.
    """
    def __init__(self, title, year):
        self.__title = title
        self.__year = year
        self.__genre = ['sci-fi','romantic','horror','comedy','action']

    @property
    def get_title(self):
        return self.__title

    def __str__(self):
        return self.__title

    def is_genre(self,genre):
        return genre in self.__genre

# wait for delete
