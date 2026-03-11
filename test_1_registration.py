from Home_Page import Home_Page
from Login_Page import Login_Page
from Registration_Page import Registration
from conftest import *

def test_register_user(open_page):
    home = Home_Page(open_page)
    home.register_button()
    register = Registration(open_page)
    register.email(current_email)
    register.surname(current_surname)
    register.name(current_name)
    register.password(current_password)
    register.check_female()
    register.register()
    register.logout()