from configuration import Configuration
import instance_globals

with open('test_data/test_parameters.json') as parameters_json:
    instance_globals.init(parameters_json.read())

print('==Parameters==')
for parameter, value in instance_globals.parameters.items():
    print(parameter, '->', value)

with open('test_data/test_config.json') as configuration_json:
    configuration = Configuration(configuration_json.read())

print('\n==Utilities==')
for utility in configuration.utilities:
    print(utility.name, '->', utility.weight_value)

print('\n==Actions==')
for action in configuration.actions:
    print(action.name, '->', action.weight_value, action.utility_score)
