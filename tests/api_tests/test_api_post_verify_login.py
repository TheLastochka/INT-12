# API URL: https://automationexercise.com/api/verifyLogin
# Request Method: POST
# Request Parameters: email, password
# Response Code: 200
# Response Message: User exists!

import requests
import allure
import config


@allure.feature("API Tests")
@allure.story("POST: Verify Login")
def test_api_post_verify_login_correct():
    
    with allure.step("Get correct login data"):
        login_data = config.website.get_login_data()
        payload = {
            "email": login_data["email"],
            "password": login_data["password"]
        }
    
    with allure.step("Send a POST request to verify login"):
        url = f"{config.website.DOMAIN}/api/verifyLogin"
        response = requests.post(url, data=payload)

    with allure.step("Verify the response code"):
        assert response.status_code == 200, f"Failed to verify login. Response code: {response.status_code}"

    with allure.step("Verify the response message"):
        response_data = response.json()
        assert response_data["message"] == "User exists!", f"Failed to verify login. Response message: {response_data['message']}"


@allure.feature("API Tests")
@allure.story("POST: Verify Login")
def test_api_post_verify_login_incorrect():
    
    with allure.step("Get incorrect login data"):
        login_data = config.website.get_login_data()
        payload = {
            "email": login_data["email"],
            "password": login_data["password"] + '1'
        }
    
    with allure.step("Send a POST request to verify login"):
        url = f"{config.website.DOMAIN}/api/verifyLogin"
        response = requests.post(url, data=payload)

    with allure.step("Verify the response code"):
        assert response.status_code == 200, f"Failed to verify login. Response code: {response.status_code}"


    with allure.step("Verify the response message"):
        response_data = response.json()
        print(response_data)
        assert response_data["message"] == "User not found!", f"Failed to verify login. Response message: {response_data['message']}"
