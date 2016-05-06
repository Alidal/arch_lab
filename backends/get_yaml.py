import yaml


def get():
    with open("backends/db.yaml", "r") as yaml_file:
        return yaml.load(yaml_file)


def set(_dict):
    with open("backends/db.yaml", "w") as yaml_file:
        yaml.dump(_dict, yaml_file)
