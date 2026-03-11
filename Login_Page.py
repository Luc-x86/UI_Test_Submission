from playwright.sync_api import Page, expect

from conftest import current_email


class Login_Page():
    def __init__(self, page: Page):
        self.page = page

    def email(self, email):
        self.page.locator("//input[@id='Email']").fill(email)

    def password(self, password):
        self.page.locator("//input[@id='Password']").fill(password)

    def login_button(self):
        self.page.locator("//input[@class='button-1 login-button']").click()

    def verify_login_page(self):
        self.page.wait_for_selector(
            "body > div.master-wrapper-page > div.master-wrapper-content > div.header > div.header-links-wrapper > div.header-links > ul > li:nth-child(1) > a")
        expect(self.page.locator("body > div.master-wrapper-page > div.master-wrapper-content > div.header > div.header-links-wrapper > div.header-links > ul > li:nth-child(1) > a")).to_have_text(current_email)