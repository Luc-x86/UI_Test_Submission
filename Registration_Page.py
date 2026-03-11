from playwright.sync_api import Page, expect
from conftest import *

class Registration:
    def __init__(self, page: Page):
        self.page = page

    def check_male(self):
        self.page.locator(malecheck).click()

    def check_female(self):
        self.page.locator(femalecheck).click()

    def name(self, myname):
        self.page.locator(name_field).fill(myname)

    def surname(self, mysurname):
        self.page.locator(surname_field).fill(mysurname)

    def email(self, email):
        self.page.locator(email_field).fill(email)

    def password(self, word_of_pass):
        self.page.locator(password_field).fill(word_of_pass)
        self.page.locator(confirm_password_field).fill(word_of_pass)

    def register(self):
        self.page.locator(register_button).click()

    def verify(self):
        self.page.wait_for_selector("//input[@class='button-1 register-continue-button']")
        expect(self.page.locator("//div[@class='result']")).to_have_text("Your registration completed")

    def logout(self):
        self.page.locator(logout_button).click()
        self.page.wait_for_selector(register_button)
        expect(self.page.locator(register_button)).to_have_text("Register")


