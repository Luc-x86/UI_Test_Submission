from Cart_Page import Cart
from Electronics_Page import Cameras_Page
from Home_Page import Home_Page
from Login_Page import Login_Page
from Registration_Page import Registration
from conftest import *

def test_purchase_camera(open_page):
    home = Home_Page(open_page)
    home.login_button()
    login_session = Login_Page(open_page)
    login_session.email(current_email)
    login_session.password(current_password)
    login_session.login_button()
    home = Home_Page(open_page)
    home.register_button()
    cameras_page = Cameras_Page(open_page)
    cameras_page.navigate()
    cameras_page.add_camera()
    checkout = Cart(open_page)
    checkout.navigate()
    checkout.checkout()
    checkout.billing_details()
    checkout.address()
    checkout.shipping_method()
    checkout.payment_method()
    checkout.payment_details()
    checkout.confirm()
    checkout.validate_order()
