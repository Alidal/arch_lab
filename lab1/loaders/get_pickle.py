import pickle


def get():
    with open("db.pkl", "r") as pickle_file:
        return pickle.loads(pickle_file)


def set(_dict):
    with open("db.pkl", "w") as pickle_file:
        pickle.dumps(_dict, pickle_file)
