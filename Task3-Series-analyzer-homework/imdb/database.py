import json
from pathlib import Path


class IMDBDatabase:
    """
    Basic implementation of imdb.com database, which loads locally stored data about series and is able to provide all
    data about all series.
    """

    def __init__(self, path_to_local_data_file=Path("imdb", "imdb_data.json")):
        self._series_data = self._load_series_data_from_local_data_file(path_to_local_data_file)

    @staticmethod
    def _load_series_data_from_local_data_file(path_to_local_data_file):
        with open(path_to_local_data_file) as data_file:
            return json.load(data_file)

    @staticmethod
    def get_database_name():
        return "imdb.com"

    def get_series_data(self):
        return self._series_data["series"]
