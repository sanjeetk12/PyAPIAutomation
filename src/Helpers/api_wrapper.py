import requests
import json


def get_request(url, auth, in_json, payload):
    post_response_data = requests.get(url=url, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return post_response_data.json()
    return post_response_data


def patch_request(url, auth, in_json, payload):
    patch_response_data = requests.get(url=url, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


def delete_request(url, auth, in_json, payload):
    delete_response_data = requests.get(url=url, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data
