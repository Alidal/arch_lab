from yaml import load, dump


def get():
    with open("backends/db.yaml", "r") as yaml_file:
        return load(yaml_file)


def set(_dict):
    with open("backends/db.yaml", "w") as yaml_file:
        dump(_dict, yaml_file)
