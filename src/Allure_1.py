import pytest
import allure

def test_addition ():
    assert 1 + 1 ==6

@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@pytest.mark.smoke
def test_multiply():
    assert 1 * 2 ==2

@pytest.mark.smoke
def test_sub():
    assert 1 -1 ==0

def test_123():
    assert 'shubham' == 'shubham'