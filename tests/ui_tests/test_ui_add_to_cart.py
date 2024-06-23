import allure
from playwright.sync_api import Page
from pages.products import ProductsPage
from pages.cart import CartPage

@allure.feature("UI Tests")
@allure.story("Add to Cart")
def test_ui_add_to_cart(page: Page, clear_cart=True):

    with allure.step("Verify that cart is empty"):
        CartPage().open(page)
        if not page.locator("#cart_info", has_text="Cart is empty!").is_visible():
            with allure.step("Clear cart"):
                while page.locator(".cart_quantity_delete").is_visible():
                    page.click(".cart_quantity_delete")
        else:
            with allure.step("Cart is empty"):
                pass
    
    products_in_cart = []
    with allure.step("Add products to cart"):
        ProductsPage().open(page)
        products = page.locator(".single-products")
        assert products.count() >= 2
        with allure.step("Add products"):
            for i in range(2):
                with allure.step(f"Add product {i+1} to cart"):
                    p = products.nth(i).locator(".productinfo")
                    products_in_cart.append({
                        "name": p.locator("p").inner_text(),
                        "price": p.locator("h2").inner_text()
                    })
                    p.locator(".add-to-cart").click()
                    page.wait_for_timeout(1000)
                    page.get_by_text("Continue Shopping").click()

    with allure.step("Verify products in cart"):
        CartPage().open(page)
        with allure.step("Check prices and names"):
            for i in range(2):
                with allure.step(f"Check product {i+1}"):
                    product = page.locator(f"#product-{i+1}")
                    assert product.locator(".cart_description a").inner_text() == products_in_cart[i]["name"]
                    assert product.locator(".cart_price p").inner_text() == products_in_cart[i]["price"]

    if clear_cart:
        with allure.step("Remove products from cart"):
            for i in range(2):
                with allure.step(f"Remove product {i+1}"):
                    page.locator(f"#product-{i+1}").locator(".cart_quantity_delete").click()
                    page.wait_for_timeout(1000)
    
        with allure.step("Verify that cart is empty"):
            assert page.locator("#cart_info", has_text="Cart is empty!").is_visible()
