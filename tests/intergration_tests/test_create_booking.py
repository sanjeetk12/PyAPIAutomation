import pytest
import warnings

import requests

from src.Constants.apiconstanst import url_create_booking, base_url, url_update_delete_booking, url_create_token
from src.Helpers.api_wrapper import post_request, patch_request, delete_request, get_request
from src.Helpers.payload_manager import create_booking, patch_update, create_token, get_booking
from src.Helpers.utils import common_headers, token_headers
from src.Helpers.common_verification import verify_http_code, verify_key

# Declare the global variable booking_id
booking_id = None


class TestIntegration(object):

    @pytest.fixture
    def test_create_booking_tc1(self):
        global booking_id
        response = post_request(url_create_booking(), header=common_headers(), auth=None, in_json=False,
                                payload=create_booking())
        verify_http_code(response, 200)
        booking_id = response.json()["bookingid"]
        print(response.json())
        verify_key(booking_id)
        return booking_id

    @pytest.fixture
    def test_create_token_tc2(self):
        response = post_request(url_create_token(), header=common_headers(), auth=None, in_json=False,
                                payload=create_token())
        verify_http_code(response, 200)
        token = response.json()["token"]
        print(token)
        return response.json()["token"]

    def test_patch_update_tc3(self, test_create_booking_tc1, test_create_token_tc2):
        response = patch_request(url_update_delete_booking(str(test_create_booking_tc1)),
                                 header=token_headers(test_create_token_tc2),
                                 auth=None,
                                 in_json=False,
                                 payload=patch_update())
        verify_http_code(response, 200)
        print(response.json())

    def test_get_tc4(self, test_create_booking_tc1):
        global booking_id
        response = get_request(url_update_delete_booking(str(booking_id)),
                               header=common_headers(),
                               auth=None,
                               in_json=False,
                               payload=get_booking())
        verify_http_code(response, 200)
        print(response.json())
# def test_create_booking_tc3(self):
#     assert True == False
