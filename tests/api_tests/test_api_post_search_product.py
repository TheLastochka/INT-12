import requests
import allure
import pytest
import config


@allure.feature("API Tests")
@allure.story("POST: Search Product")
@pytest.mark.parametrize("search_product", [
    "Printed Off Shoulder Top - White",
    "Pure Cotton V-Neck T-Shirt",
    "Soft Stretch Jeans",
    ])
def test_api_post_search_product(search_product: str):
    url = f"{config.website.DOMAIN}/api/searchProduct"
    payload = {"search_product": search_product}
    response = requests.post(url, data=payload)

    with allure.step("Verify the response code"):
        assert response.status_code == 200, f"Failed to search product. Response code: {response.status_code}"
    with allure.step("Verify the response data"):
        response_data = response.json()
        resp_products = response_data["products"]
        for product in resp_products:
            assert search_product.lower() in product["name"].lower(), f"Failed to search product. Product name: {product['name']}"