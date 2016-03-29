import json


def get():
	"""
    Read data from file.
    """
    with open("backends/db.json", "r") as json_file:
        return json.load(json_file)


def set(_json):
	"""
    Write passed data to file.
    """
    with open("backends/db.json", "w") as json_file:
        json.dump(_json, json_file)
