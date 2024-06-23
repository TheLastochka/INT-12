import allure
from playwright.sync_api import Page, expect
import config
from pages.index import IndexPage

class LoginPage:

    def open(self, page: Page) -> None:

        if config.website.DOMAIN not in page.url:
            IndexPage().open(page)

        with allure.step("Check if logged in"):
            logout_btn = page.get_by_role("link", name="Logout")
            if logout_btn.is_visible():
                with allure.step("Logout"):
                    page.click("text=Logout")
                    page.wait_for_timeout(500)
                    expect(page.get_by_role("link", name="Signup / Login")).to_be_visible()
            else:
                with allure.step("Already logged out"):
                    expect(page.get_by_role("link", name="Signup / Login")).to_be_visible()

        with allure.step("Open Signup/Login page"):
            btn = page.get_by_role("link", name="Signup / Login")
            expect(btn).to_be_visible()
            btn.click()
            expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()

    