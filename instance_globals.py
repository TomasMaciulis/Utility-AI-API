import json

global parameters


def init(parameters_json):
    global parameters
    parameters = json.loads(parameters_json)
