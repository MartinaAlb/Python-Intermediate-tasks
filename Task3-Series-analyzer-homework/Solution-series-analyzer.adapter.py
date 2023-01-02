"""
This code is a solution to given homework / as you can see at series_analyzer.py
All other codes and files in this directory were given by the lector.
Language Python.
"""


import json

from imdb.database import IMDBDatabase


class CSFDDatabase:
    """
    Basic implementation of csfd.cz database, which loads locally stored data about series and can provide users rating
    of a series.
    """

    def __init__(self, path_to_local_data_file="csfd_data.json"):
        self._series_data = self._load_series_data_from_local_data_file(path_to_local_data_file)


    @staticmethod
    def _load_series_data_from_local_data_file(path_to_local_data_file):
        with open(path_to_local_data_file) as data_file:
            return json.load(data_file)

    def get_database_name(self):
        return "csfd.cz"

    def get_users_rating(self, series_name):
        try:
            return self._series_data["series"][series_name]["average_rating_out_of_ten"]
        except KeyError:
            raise Exception(f"Series '{series_name}' is not in CSFD database!")


class IMDBDatabase(IMDBDatabase):

    def get_users_rating(self, series_name):
        try:
            return self._series_data["series"][series_name]["average_rating"]
        except KeyError:
            raise Exception(f"Series '{series_name}' is not in IMDB database!")

def print_databases_rating(series_databases: list, series_name: str):
    """
    Prints rating of series in each available database and also calculates average rating from all databases.
    """
    print(f"Series '{series_name}' ratings:")

    total_rating = 0
    for database in series_databases:
        db_rating = database.get_users_rating(series_name)
        print(f"\tRating in database {database.get_database_name()}: {db_rating}")
        total_rating += db_rating

    series_rating_average = total_rating / len(series_databases)
    print(f"\tAverage rating of series is {series_rating_average:.2f}")


def main():
    # calculate average rating of users of given series list from all available data sources (series databases)
    series_of_interest = ["House of dragon", "The lord of the rings: Rings of power", "Narcos"]
    series_databases = [CSFDDatabase(), IMDBDatabase()]
    for series_name in series_of_interest:
        print_databases_rating(series_databases, series_name)


if __name__ == "__main__":
    main()