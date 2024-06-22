import allure
from playwright.sync_api import Page, expect
import re

# @allure.feature("Playwright")
# @allure.story("Test if Playwright website is up")
# def test_has_title(page: Page):

#     with allure.step("Navigate to Playwright website"):
#         page.goto("https://playwright.dev/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))

# @allure.feature("Playwright")
# @allure.story("Test if Playwright.get_started_link is working")
# def test_get_started_link(page: Page):

#     with allure.step("Navigate to Playwright website"):
#         page.goto("https://playwright.dev/")

#     # Click the get started link.
#     with allure.step("Click on Get started link"):
#         page.get_by_role("link", name="Get started").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Introduction")).to_be_visible()


def test_browser_open(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))