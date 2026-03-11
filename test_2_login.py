from Home_Page import Home_Page
from Login_Page import Login_Page
from conftest import *

def test_login_user(open_page):
    home = Home_Page(open_page)
    home.login_button()
    login_session = Login_Page(open_page)
    login_session.email(current_email)
    login_session.password(current_password)
    login_session.login_button()