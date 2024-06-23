import allure
from playwright.sync_api import Page, expect
import config
from tests.ui_tests.test_ui_add_to_cart import test_ui_add_to_cart
from tests.ui_tests.test_ui_login import test_ui_login_correct
import random


@allure.feature('UI Tests')
@allure.story('Place Order')
def test_ui_place_order(page: Page, card_payment):

        with allure.step('Login'):
                test_ui_login_correct(page)

        with allure.step('Add to cart'):
            test_ui_add_to_cart(page, clear_cart=False)

        with allure.step('Place order'):
            with allure.step('Checkout'):
                page.locator('a.check_out').click()
                page.wait_for_timeout(500)
            with allure.step('Add description'):
                page.fill('textarea', f'This is a test order #{random.randint(1, 1000)}')
            with allure.step('Place order'):
                page.get_by_role('link', name='Place Order').click()
                page.wait_for_timeout(500)
            with allure.step('Fill payment data'):
                page.fill('input[data-qa="name-on-card"]', card_payment['name'])
                page.fill('input[data-qa="card-number"]', card_payment['card_number'])
                page.fill('input[data-qa="expiry-month"]', card_payment['expiration_mm'])
                page.fill('input[data-qa="expiry-year"]', card_payment['expiration_yyyy'])
                page.fill('input[data-qa="cvc"]', card_payment['cvc'])
                page.click('button[data-qa="pay-button"]')
                page.wait_for_timeout(2000)
            with allure.step('Check order success'):
                success = page.locator('b', has_text='Order Placed!')
                expect(success).to_be_visible()
            
            

            