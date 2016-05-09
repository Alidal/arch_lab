"""
Module for using Yaml as serializer. Provides methods for retrieving
data and writing.
"""
import yaml


class YamlSerializer:
    def __init__(self, file_name="backends/db.yaml"):
        self.file_name = file_name

    def read(self):
        """
        Read data from file.
        """
        with open(self.file_name, "r") as yaml_file:
            return yaml.load(yaml_file)


    def write(self, _dict):
        """
        Write passed data to file.
        """
        with open(self.file_name, "w") as yaml_file:
            yaml.dump(_dict, yaml_file)
