# Http Status code
def verify_http_code(response_data, excepted_data):
    assert response_data.status_code == int(excepted_data), "Excepted Status :" + excepted_data


#

def verify_key(key):
    assert key != 0, "key is not empty" + key
    assert key > 0, "key should be greater than key" + key