"""
Module for using json as serializer. Provides methods for retrieving
data and writing.
"""
import json


class JsonSerializer:
    def __init__(self, file_name="backends/db.json"):
        self.file_name = file_name

    def read(self):
        """
        Read data from file.
        """
        with open(self.file_name, "r") as json_file:
            return json.load(json_file)


    def write(self, _json):
        """
        Write passed data to file.
        """
        with open(self.file_name, "w") as json_file:
            json.dump(_json, json_file)
