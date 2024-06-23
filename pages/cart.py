import allure
from playwright.sync_api import Page, expect
import config
from pages.index import IndexPage

class CartPage:

    def open(self, page: Page) -> None:

        if config.url.DOMAIN not in page.url:
            IndexPage().open(page)

        with allure.step("Open Cart page"):
            btn = page.get_by_role("link", name="Cart")
            expect(btn).to_be_visible()
            btn.click()
            expect(page.locator("#cart_items")).to_be_visible()

    