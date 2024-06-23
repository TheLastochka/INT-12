from playwright.sync_api import Page, expect
import allure
import config


class IndexPage:

    def open(self, page: Page) -> None:
         with allure.step("Open the website"):
            page.goto(config.website.DOMAIN)
            expect(page.get_by_role("heading", name="AutomationExercise")).to_be_visible()

    