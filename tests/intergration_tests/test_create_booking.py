import pytest
import warnings

import requests

from src.Constants.apiconstanst import url_create_booking, base_url, url_update_delete_booking
from src.Helpers.api_wrapper import post_request, patch_request, delete_request
from src.Helpers.payload_manager import create_booking, patch_update
from src.Helpers.utils import common_headers
from src.Helpers.common_verification import verify_http_code, verify_key


class TestIntegration(object):

    @pytest.fixture
    def test_create_booking_tc1(self):
        response = post_request(url_create_booking(), header=common_headers(), auth=None, in_json=False,
                                payload=create_booking())
        verify_http_code(response, 200)
        booking_id = response.json()["bookingid"]
        print(response.json())
        verify_key(booking_id)
        return booking_id

    def test_create_booking_tc2(self):
        response = patch_request(url_update_delete_booking(self.test_create_booking_tc1), header=common_headers(),
                                 auth={
                                     "username": "admin",
                                     "password": "password123"
                                 },
                                 in_json=False,
                                 payload=patch_update())
        verify_http_code(response, 200)

# def test_create_booking_tc3(self):
#     assert True == False
