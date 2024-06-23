# API URL: https://automationexercise.com/api/verifyLogin
# Request Method: DELETE
# Response Code: 405
# Response Message: This request method is not supported.

import requests
import allure
import config


@allure.feature("API Tests")
@allure.story("DELETE: Verify Login")
def test_api_delete_verify_login():
    
    with allure.step("Send a DELETE request to verify login"):
        url = f"{config.website.DOMAIN}/api/verifyLogin"
        response = requests.delete(url)
    
    response_data = response.json()

    with allure.step("Verify the response code"):
        assert response.status_code == 200, f"Failed to verify login. Response code: {response.status_code}"
        assert response_data["responseCode"] == 405, f"Failed to verify login. Response code: {response_data['responseCode']}"
    with allure.step("Verify the response message"):
        assert response_data["message"] == "This request method is not supported.", f"Failed to verify login. Response message: {response_data['message']}"