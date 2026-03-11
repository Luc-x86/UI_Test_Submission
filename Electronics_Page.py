from playwright.sync_api import Page

class Cameras_Page:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.locator("body > div.master-wrapper-page > div.master-wrapper-content > div.header-menu > ul.top-menu > li:nth-child(3) > a").hover()
        self.page.locator("//a[@class='hover']").click()
        self.page.wait_for_selector("body > div.master-wrapper-page > div.master-wrapper-content > div.master-wrapper-main > div.center-2 > div.page.category-page > div.page-body > div.sub-category-grid > div:nth-child(1) > div > h2 > a").click()
        #self.page.goto("https://demowebshop.tricentis.com/camera-photo")

    def add_camera(self):
        self.page.wait_for_selector("body > div.master-wrapper-page > div.master-wrapper-content > div.master-wrapper-main > div.center-2 > div.page.category-page > div.page-body > div.product-grid > div:nth-child(3) > div > div.details > h2 > a").click()
        self.page.wait_for_selector("//input[@id='add-to-cart-button-18']").focus()
        self.page.wait_for_selector("//input[@id='add-to-cart-button-18']").click()