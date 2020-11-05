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

    for bucket in configuration.buckets:
        print(bucket.name, ": ", bucket.utility_score, " -> ", bucket.utility_score_int)

    return {"bucket": ActionPicker(configuration.buckets).pick_weighted_random().name}


if __name__ == "__main__":
    app.run(debug=True)
