import json

global parameters


def init(parameters_dict):
    global parameters

    for key in parameters_dict:
        try:
            parameters_dict[key] = int(parameters_dict[key])
        except:
            continue
    parameters = parameters_dict
