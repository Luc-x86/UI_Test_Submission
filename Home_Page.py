from playwright.sync_api import Page, expect

class Home_Page:
    def __init__(self, page: Page):
        self.page = page

    def register_button(self):
        self.page.locator('body > div.master-wrapper-page > div.master-wrapper-content > div.header > div.header-links-wrapper > div.header-links > ul > li:nth-child(1) > a').click()

    def login_button(self):
        self.page.locator("//a[@class='ico-login']").click()