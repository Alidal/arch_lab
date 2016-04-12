"""
Module for using pickle as serializer. Provides methods for retrieving
data and writing.
"""
import pickle


def get():
    with open("backends/db.pkl", "rb") as pickle_file:
        return pickle.load(pickle_file)


def set(_dict):
    with open("backends/db.pkl", "wb") as pickle_file:
        pickle.dump(_dict, pickle_file)
