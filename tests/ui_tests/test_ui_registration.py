import allure
import pytest
from playwright.sync_api import Page, expect
import config
from pages.login import LoginPage

@allure.feature("UI Tests")
@allure.story("Registration")
def test_ui_registration(page: Page, username: str, password: str) -> None:
    
    LoginPage().open(page)
    email = f"{username}@mail.ru"
    
    with allure.step("Fill in start registration form"):
        page.fill('form[action="/signup"] input[data-qa="signup-name"]', username)
        page.fill('form[action="/signup"] input[data-qa="signup-email"]', email)
        page.click('button[data-qa="signup-button"]')
        page.wait_for_timeout(500)
        expect(page.locator('b', has_text='Enter Account Information')).to_be_visible()
    
    with allure.step("Fill in account information form"):
        page.click('input[id="id_gender1"]')
        page.fill('form[action="/signup"] input[data-qa="password"]', password)
        page.select_option('select[data-qa="days"]','1')
        page.select_option('select[data-qa="months"]','January')
        page.select_option('select[data-qa="years"]','2000')

    with allure.step("Fill in address information form"):
        page.fill('input[data-qa="first_name"]','Alexander')
        page.fill('input[data-qa="last_name"]','Pushkin')
        page.fill('input[data-qa="company"]','ITMO')
        page.fill('input[data-qa="address"]','abcdef, 129339, abcdef')
        page.select_option('select[id="country"]','United States')
        page.fill('input[id="state"]','California')
        page.fill('input[id="city"]','Los Angeles')
        page.fill('input[id="zipcode"]','111111')
        page.fill('input[id="mobile_number"]','+79211231212')
    
    with allure.step("Submit registration form"):
        page.click('button[type="submit"]')
    
    with allure.step("Check registration success"):
        expect(page.locator('b', has_text='Account Created')).to_be_visible()
        print()
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Password: {password}")

        config.website.add_login_data(username, email, password)

