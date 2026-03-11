from playwright.sync_api import Page, expect
from conftest import *

class Registration:
    def __init__(self, page: Page):
        self.page = page

    def check_male(self):
        self.page.locator("//input[@id='gender-male']").click()

    def check_female(self):
        self.page.locator("//input[@id='gender-female']").click()

    def name(self, myname):
        self.page.locator("//input[@id='FirstName']").fill(myname)

    def surname(self, mysurname):
        self.page.locator("//input[@id='LastName']").fill(mysurname)

    def email(self, email):
        self.page.locator("//input[@id='Email']").fill(email)

    def password(self, word_of_pass):
        self.page.locator("//input[@id='Password']").fill(word_of_pass)
        self.page.locator("//input[@id='ConfirmPassword']").fill(word_of_pass)

    def register(self):
        self.page.locator("//input[@id='register-button']").click()

    def verify(self):
        self.page.wait_for_selector("//input[@class='button-1 register-continue-button']")
        expect(self.page.locator("//div[@class='result']")).to_have_text("Your registration completed")

    def logout(self):
        self.page.locator("//a[@class='ico-logout']").click()
        self.page.wait_for_selector("//a[@class='ico-register']")
        expect(self.page.locator("//a[@class='ico-register']")).to_have_text("Register")