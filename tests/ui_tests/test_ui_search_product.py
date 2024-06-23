import allure
import pytest
from playwright.sync_api import Page, expect
from pages.products import ProductsPage

@allure.feature("UI Tests")
@allure.story("Search Product")
@pytest.mark.parametrize("product", [
    "Men Tshirt",
    "Frozen Tops For Kids",
    "Soft Stretch Jeans"
    ])
def test_ui_search_product(page: Page, product: str):
    
    ProductsPage().open(page)

    with allure.step(f"Search for a product '{product}'"):
        page.fill("#search_product", product)
        page.click("#submit_search")

    with allure.step("Verify search results"):
        expect(page.locator(".single-products", has_text=product)).to_be_visible()
