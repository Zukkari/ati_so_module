import json


def read_config():
    file = open("config.json", "r")
    return json.loads(file.read())


def get_node_value(path):
    # Retrieves value from configuration based on path e.g. 'conf:languages:from' returns 'ee'
    nodes = path.split(":")

    res = read_config()
    for node in nodes:
        res = res[node]

    return res
