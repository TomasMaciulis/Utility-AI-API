from flask import Flask, request
from utility_ai.models.configuration import Configuration
from utility_ai import instance_globals
from utility_ai.action_picker import ActionPicker

app = Flask(__name__)


@app.route('/action', methods=['POST'])
def action():
    instance_globals.init(request.args)

    with open('test_data/test_config.json') as configuration_json:
        configuration = Configuration(configuration_json.read())

    picked_bucket = ActionPicker(configuration.buckets).pick_weighted_random()
    picked_action = ActionPicker(picked_bucket.actions).pick_weighted_random()

    return {"bucket": picked_bucket.name,
            "action": picked_action.name}


if __name__ == "__main__":
    app.run(debug=True)
