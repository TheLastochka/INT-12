import allure
from playwright.sync_api import Page, expect
import config
from pages.index import IndexPage

class ProductsPage:

    def open(self, page: Page) -> None:

        if config.website.DOMAIN not in page.url:
            IndexPage().open(page)

        with allure.step("Open Products page"):
            btn = page.get_by_role("link", name="Products")
            expect(btn).to_be_visible()
            btn.click()
            expect(page.get_by_role("heading", name="ALL PRODUCTS")).to_be_visible()

    