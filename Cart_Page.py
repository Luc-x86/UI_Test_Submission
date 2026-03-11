from playwright.sync_api import Page, expect
from conftest import *

class Cart:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://demowebshop.tricentis.com/cart")

    def checkout(self):
        self.page.wait_for_selector("#termsofservice").check()
        self.page.wait_for_selector("//button[@id='checkout']").click()

    def details(self):
        self.page.wait_for_selector("//select[@id='BillingNewAddress_CountryId']").click()
        self.page.select_option("//select[@id='BillingNewAddress_CountryId']", value=current_country)
        self.page.locator("//input[@id='BillingNewAddress_City']").fill(current_city)
        self.page.locator("//input[@id='BillingNewAddress_Address1']").fill(current_address_line_1)
        self.page.locator("//input[@id='BillingNewAddress_ZipPostalCode']").fill(current_zip_code)
        self.page.locator("//input[@id='BillingNewAddress_PhoneNumber']").fill(current_phone_number)
        self.page.locator("#billing-buttons-container > input").click()
        self.page.wait_for_selector("#shipping-buttons-container > input").click()
        self.page.wait_for_selector("#shipping-method-buttons-container > input").click()
        self.page.wait_for_selector("//input[@id='paymentmethod_2']").check()
        self.page.wait_for_selector("#payment-method-buttons-container > input").click()
        self.page.wait_for_selector("#CreditCardType").click()
        self.page.select_option("#CreditCardType", value=current_card_type)
        self.page.locator("#CardholderName").fill(current_cardholder)
        self.page.locator("#CardNumber").fill(current_card_number)
        self.page.locator("#ExpireMonth").click()
        self.page.select_option("#ExpireMonth", value=current_expiry_month)
        self.page.wait_for_selector("#ExpireYear").click()
        self.page.select_option("#ExpireYear", value=current_expiry_year)
        self.page.wait_for_selector("#CardCode").fill(current_cvv)
        self.page.locator("#payment-info-buttons-container > input").click()
        self.page.wait_for_selector("#confirm-order-buttons-container > input").click()

    def confirm_order(self):
        expect(self.page.wait_for_selector("body > div.master-wrapper-page > div.master-wrapper-content > div.master-wrapper-main > div > div > div.page-body.checkout-data > div > div.title > strong")).to_have_text("Your order has been successfully processed!")



