import allure
import pytest
from playwright.sync_api import Page, expect
import config

@allure.feature("UI Tests")
@allure.story("Search Product")
@pytest.mark.parametrize("product", [
    "Men Tshirt",
    "Frozen Tops For Kids",
    "Soft Stretch Jeans"
    ])
def test_search_product(page: Page, product: str):
    with allure.step("Open the website"):
        page.goto(config.url.DOMAIN)
        expect(page.get_by_role("heading", name="AutomationExercise")).to_be_visible()

    with allure.step("Click on 'Products' button"):
        expect(page.get_by_role("link", name="Products"), "should be visible").to_be_visible()
        page.get_by_role("link", name="Products").click()
        expect(page.get_by_role("heading", name="ALL PRODUCTS")).to_be_visible()

    with allure.step(f"Search for a product '{product}'"):
        page.fill("#search_product", product)
        page.click("#submit_search")

    with allure.step("Verify search results"):
        expect(page.locator(".single-products", has_text=product)).to_be_visible()
