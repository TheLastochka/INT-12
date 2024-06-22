# API 1: Get All Products List
# API URL: https://automationexercise.com/api/productsList
# Request Method: GET
# Response Code: 200
# Response JSON: All products list

import requests
import pytest
import allure
import config

@allure.feature("API Tests")
@allure.story("Get All Products List")
def test_get_all_products_list():
    url = f"{config.url.DOMAIN}/api/productsList"
    response = requests.get(url)
    assert response.status_code == 200, f"Failed to get all products list. Response code: {response.status_code}"
    assert response.json(), "Failed to get all products list. Response is empty"
    print(response.json())

    # with allure.step("Verify the response code is 200"):
    #     assert response.status_code == 200, f"Failed to get all products list. Response code: {response.status_code}"
    #
    # with allure.step("Verify the response is not empty"):
    #     assert response.json(), "Failed to get all products list. Response is empty"