from yaml import load, dump


def get():
    with open("db.yaml", "r") as yaml_file:
        return load(yaml_file)


def set(_dict):
    with open("db.yaml", "w") as yaml_file:
        dump(_dict, yaml_file)
