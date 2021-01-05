from flask import Flask, request
import json
from utility_ai.models.configuration import Configuration
from utility_ai import instance_globals
from utility_ai.action_picker import ActionPicker
import utility_ai.database_operations as DatabaseOperations

app = Flask(__name__)


@app.route('/action', methods=['GET'])
def action():
    parameters = request.get_json()
    user = DatabaseOperations.get_user_config(parameters['key'])

    if not user:
        return {
            "status": "user not found"
        }, 401
    user_config_uri = user[0]

    instance_globals.init(parameters)

    with open(user_config_uri) as configuration_json:
        configuration = Configuration(configuration_json.read())

    print(instance_globals.parameters)
    for bucket in configuration.buckets:
        print(bucket.name, bucket.utility_score)
        print("*******************")
        for action in bucket.actions:
            print(action.name, action.utility_score)
        print("\n")

    picked_bucket = ActionPicker(configuration.buckets).pick_weighted_random()
    picked_action = ActionPicker(picked_bucket.actions).pick_weighted_random()

    return {
        "bucket": picked_bucket.name,
        "action": picked_action.name
    }


@app.route('/config', methods=['GET'])
def config():
    parameters = request.get_json()
    user = DatabaseOperations.get_user_config(parameters['key'])

    if not user:
        return {
                   "status": "user not found"
               }, 401
    user_config_uri = user[0]

    with open(user_config_uri) as configuration_json:
        return json.loads(configuration_json.read())


@app.route('/create-user', methods=['POST'])
def create_user():
    parameters = request.get_json()
    result = DatabaseOperations.create_user(parameters['key'], parameters['configuration'])

    if result:
        status = 'success'
    else:
        status = 'failed'

    return {
        "status": status
    }

if __name__ == "__main__":
    app.run(debug=True)
