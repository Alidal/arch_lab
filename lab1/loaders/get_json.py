import json


def get():
    with open("db.json", "r") as json_file:
        return json.load(json_file)


def set(_json):
    with open("db.json", "w") as json_file:
        json.dump(_json, json_file)
