import random
import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture(scope='session',autouse=True)
def open_page(playwright: Playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demowebshop.tricentis.com/")
    yield page

def email_gen():
    length = random.randint(1, 7)
    word = ""
    for i in range(length):
        word += random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"])
        word += random.choice(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
    gen_email = f"{word}@gmail.com"
    return gen_email

current_email = email_gen()
current_password = "Tosca1234!"
current_name = "Barbara"
current_surname = "Gordon"
current_country = "Austria"
current_city = "Vienna"
current_address_line_1 = "Vienna Street"
current_zip_code = "1234"
current_phone_number = "001122334455"
current_card_type = "Visa"
current_cardholder = "Barbara Gordon"
current_card_number = "4485564059489345"
current_expiry_month = "04"
current_expiry_year = "2026"
current_cvv = "123"



