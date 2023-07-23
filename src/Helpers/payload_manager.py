def create_booking():
    payload = {

            "firstname": "San",
            "lastname": "Kosi",
            "totalprice": 112,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2018-01-01"
            },
            "additionalneeds": "Breakfast"
        }

    return payload

def patch_update():
    payload ={
        "firstname": "San",
        "lastname": "Kosi"

    }
    return payload

