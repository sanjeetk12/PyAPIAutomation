# Helps to read json files and provide you the json data

import json


def get_pay_load_auth():
    # Read from the auth.json and return json
    file_date = open("src/resources/auth.json")
    data = json.load(file_date)
    file_date.close()
    return data

