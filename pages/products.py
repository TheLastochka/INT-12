import allure
from playwright.sync_api import Page, expect
import config
from pages.index import IndexPage

class ProductsPage:

    def open(self, page: Page) -> None:
        IndexPage().open(page)
        with allure.step("Open Products page"):
            expect(page.get_by_role("link", name="Products")).to_be_visible()
            page.get_by_role("link", name="Products").click()
            expect(page.get_by_role("heading", name="ALL PRODUCTS")).to_be_visible()

    