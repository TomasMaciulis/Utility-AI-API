import json

global parameters


def init(parameters_dict):
    global parameters

    parameters_dict = parameters_dict.to_dict()
    for key in parameters_dict:
        parameters_dict[key] = int(parameters_dict[key])

    parameters = parameters_dict
