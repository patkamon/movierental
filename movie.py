
class Movie:
    """
    A movie available for rent.
    """
    def __init__(self, title, year, genre):
        self._title = title
        self._year = year
        self._genre = genre

    @property
    def get_title(self):
        return self._title

    @property
    def get_year(self):
        return self._year

    def __str__(self):
        return self._title

    def is_genre(self,genre):
        return genre in self._genre

# wait for delete

class MovieCatalog:
    def __init__(self):
        self.catalog = self.setup()

    def setup(self):
        f = open("movies.csv", "r")
        for line in f:
            data = f.readline().strip("\n").split(",")
            id = data[0]
            title = data[1]
            year = int(data[2])
            genre = data[3]

            new_movie = {'id': id, 'title': title, 'year': year, 'genre': genre}

            return  [new_movie]

    def get_movie(self, given_title):
        try:
            found = next(item for item in self.catalog if item["title"] == given_title)
            return Movie(found['title'], found['year'], found['genre'])
        except:
            f = open("movies.csv", "r")
            for line in f:
                data =  line.strip("\n").split(",")
                id = data[0]
                title = data[1]
                year = data[2]
                genre = data[3]

                try:
                    next(item for item in self.catalog if item["id"] == id)
                except:
                    new_movie = {'id': id, 'title': title, 'year': year, 'genre': genre}
                    self.catalog.append(new_movie)

                    if title == given_title:
                        return Movie(title, year, genre)

            return Movie(given_title, "Unknown", ["Unknown"])
