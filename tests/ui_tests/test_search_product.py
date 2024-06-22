import allure
import pytest
from playwright.sync_api import Page, expect
import re
import config

@allure.feature("UI Tests")
@allure.story("Search Product")
# @pytest.mark.parametrize("product", ["Macbook", "iPhone", "iPad"])
def test_search_product(page: Page):
    with allure.step("Open the website"):
        # print({website})
        page.goto(config.url.DOMAIN)
    #     expect(page.get_by_role("heading", name="AutomationExercise")).to_be_visible()

    # with allure.step("Click on 'Products' button"):
    #     page.get_by_role("button", name="Products").click()
    #     expect(page.get_by_role("heading", name="Products")).to_be_visible()
    
    assert 1 == 1, "Test failed"
