import pytest
import requests   # -- pip install requests
import allure
from selenium import webdriver



@allure.title("API Automation through CRUD operations")
@allure.description(" verify the Create Booking ")
@pytest.mark.crud
def test_create_booking_positive():
    # Requests
    # URL
    # Headers
    # Auth
    # Payload,Data
    base_url= "https://restful-booker.herokuapp.com"
    base_path="/booking"
    Url = base_url + base_path
    Headers= {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
     }
    response= requests.post(url=Url,headers=Headers,json=payload)

    # Response Body Verification
# Status code
# Response time
# headers
# payload-Json schema validation

    assert response.status_code == 200
    print(response.headers)
    response_json = response.json()
    booking_id = response_json["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int
    firstname = response_json["booking"]["firstname"]
    assert firstname == "Jim"

@allure.title("API Automation through CRUD operations")
@allure.description(" verify the Create Booking with empty payload {} ")
@pytest.mark.crud
def test_create_booking_negative():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    Url = base_url + base_path
    Headers = {"Content-Type": "application/json"}
    payload = {}
    response = requests.post(url=Url, headers=Headers, json=payload)


    assert response.status_code == 500
    print(type(Headers))
    print(type(Url))
    print((type(payload)))

