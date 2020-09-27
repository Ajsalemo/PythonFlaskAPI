import json


def load_json():
    with open("db.json") as f:
        return json.load(f)


json_db = load_json()