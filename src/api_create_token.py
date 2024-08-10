import pytest
import requests   # -- pip install requests
import allure



@allure.title("API Automation through CRUD operations -Create token")
@allure.description(" verify the Create Token ")
@pytest.mark.crud
def create_token():
    # Requests
    # URL
    # Headers
    # Auth
    # Payload,Data
    base_url = "https://restful-booker.herokuapp.com"
    base_path ="/auth"
    Url = base_url + base_path
    Headers= {"Content-Type": "application/json"}
    payload = {
     "username" : "admin",
     "password" : "password123"
 }
    response = requests.post(url=Url,headers=Headers,json=payload)
    assert response.status_code == 200
    response_json = response.json()
    token = response_json["token"]
    print(token)
    return token

@allure.title("API Automation through CRUD operations")
@allure.description(" verify the Create Booking_ID ")
@pytest.mark.crud
def create_booking():
    # Requests
    # URL
    # Headers

    # Auth
    # Payload,Data
    base_url = "https://restful-booker.herokuapp.com"
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
    response = requests.post(url=Url,headers=Headers,json=payload)

    assert response.status_code == 200
    print(response.headers)
    response_json = response.json()
    booking_id = response_json["bookingid"]
    return booking_id

def test_update_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    # param = create_booking()
    PUT_URL = base_url+base_path
    cookie = "token=" + create_token()
    Headers = {
        "Content-Type": "application/json",
         "Cookie":"cookie"
    }
    print(Headers)
    payloads = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
     }

    response= requests.post(url=PUT_URL,headers=Headers,json=payloads)
    print(PUT_URL)
    print(response.status_code)
    assert response.status_code == 200
    data = response.json()
    # assert data ["firstname"] == "Vedant"f

