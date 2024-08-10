import pytest
import requests   # -- pip install requests
import allure



@allure.title("API test Automate by GET method ")
@allure.description("Verify If we hit GET request for booking , so in response we should the status code as 200")
# @allure.tag("NewUI", "Essentials", "Authentication")
@pytest.mark.smoke
def test_get_request():
    response = requests.get("https://restful-booker.herokuapp.com/booking/3")
    print(response.json())
    print(response.text)
    print(response.status_code)
    print(response.url)
    print(response.headers)
    response_status = response.status_code
    assert response_status == 200
 