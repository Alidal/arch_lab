"""
Module for using pickle as serializer. Provides methods for retrieving
data and writing.
"""
import pickle


class PickleSerializer:
    def __init__(self, file_name="backends/db.pkl"):
        self.file_name = file_name

    def read(self):
        """
        Read data from file.
        """
        with open(self.file_name, "rb") as pickle_file:
            return pickle.load(pickle_file)


    def write(self, _dict):
        """
        Write passed data to file.
        """
        with open(self.file_name, "wb") as pickle_file:
            pickle.dump(_dict, pickle_file)
