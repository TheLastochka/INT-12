import allure
from playwright.sync_api import Page, expect
import config
from pages.login import LoginPage

@allure.feature('UI Tests')
@allure.story('Login')
def test_ui_login_correct(page: Page):
    
    LoginPage().open(page)

    with allure.step("Get correct login data"):
        login_data = config.website.get_login_data()
        username = login_data['username']
        email = login_data['email']
        password = login_data['password']
    
    with allure.step('Fill in login form'):
        page.fill('form[action="/login"] input[data-qa="login-email"]', email)
        page.fill('form[action="/login"] input[data-qa="login-password"]', password)
        page.click('button[data-qa="login-button"]')
        page.wait_for_timeout(500)
    
    with allure.step('Check login success'):
        logged_as = page.locator('a', has_text='Logged in as')
        expect(logged_as).to_be_visible()
        expect(logged_as.locator('b', has_text=username)).to_be_visible()
        

@allure.feature('UI Tests')
@allure.story('Login')
def test_ui_login_incorrect(page: Page):
        
        LoginPage().open(page)
        
        with allure.step("Get incorrect login data"):
            login_data = config.website.get_login_data()
            email = login_data['email']
            password = login_data['password'] + '1'
        
        with allure.step('Fill in login form'):
            page.fill('form[action="/login"] input[data-qa="login-email"]', email)
            page.fill('form[action="/login"] input[data-qa="login-password"]', password)
            page.click('button[data-qa="login-button"]')
            page.wait_for_timeout(500)
        
        with allure.step('Check login error'):
            error = page.locator('form[action="/login"]', has_text='Your email or password is incorrect!')
            expect(error).to_be_visible()
