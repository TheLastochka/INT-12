# API URL: https://automationexercise.com/api/brandsList
# Request Method: GET
# Response Code: 200
# Response JSON: All brands list

import requests
import allure
import config

brands = [{"id": 1, "brand": "Polo"}, {"id": 2, "brand": "H&M"}, {"id": 3, "brand": "Madame"}, {"id": 4, "brand": "Madame"}, {"id": 5, "brand": "Mast & Harbour"}, {"id": 6, "brand": "H&M"}, {"id": 7, "brand": "Madame"}, {"id": 8, "brand": "Polo"}, {"id": 11, "brand": "Babyhug"}, {"id": 12, "brand": "Babyhug"}, {"id": 13, "brand": "Allen Solly Junior"}, {"id": 14, "brand": "Kookie Kids"}, {"id": 15, "brand": "Babyhug"}, {"id": 16, "brand": "Babyhug"}, {"id": 18, "brand": "Kookie Kids"}, {"id": 19, "brand": "Allen Solly Junior"}, {"id": 20, "brand": "Kookie Kids"}, {"id": 21, "brand": "Biba"}, {"id": 22, "brand": "Biba"}, {"id": 23, "brand": "Biba"}, {"id": 24, "brand": "Allen Solly Junior"}, {"id": 28, "brand": "H&M"}, {"id": 29, "brand": "Polo"}, {"id": 30, "brand": "Polo"}, {"id": 31, "brand": "H&M"}, {"id": 33, "brand": "Polo"}, {"id": 35, "brand": "H&M"}, {"id": 37, "brand": "Polo"}, {"id": 38, "brand": "Madame"}, {"id": 39, "brand": "Biba"}, {"id": 40, "brand": "Biba"}, {"id": 41, "brand": "Madame"}, {"id": 42, "brand": "Mast & Harbour"}, {"id": 43, "brand": "Mast & Harbour"}]

@allure.feature("API Tests")
@allure.story("GET: All Brands List")
def test_api_get_all_brands():
    
    with allure.step("Send a GET request to get all brands list"):
        url = f"{config.website.DOMAIN}/api/brandsList"
        response = requests.get(url)

    with allure.step("Verify the response code"):
        assert response.status_code == 200, f"Failed to get all brands list. Response code: {response.status_code}"
    with allure.step("Verify the response data"):
        response_data = response.json()
        resp_brands = response_data["brands"]
        assert resp_brands == brands, "Failed to get all brands list. Response data is not matching with expected data"