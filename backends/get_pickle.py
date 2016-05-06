"""
Module for using pickle as serializer. Provides methods for retrieving
data and writing.
"""
import pickle


def get():
    """
    Read data from file.
    """
    with open("backends/db.pkl", "rb") as pickle_file:
        return pickle.load(pickle_file)


def set(_dict):
    """
    Write passed data to file.
    """
    with open("backends/db.pkl", "wb") as pickle_file:
        pickle.dump(_dict, pickle_file)
