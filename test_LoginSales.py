from Librariries import *
from Main.ConfigReader import ReadConfig_URL, ReadConfig_LOGIN
from PageObject.LoginPage import LoginPage
from Tests.test_BaseTest import BaseTest
import sys
sys.setrecursionlimit(10000)

class Test_Loginsales(BaseTest):

    @allure.feature("SUITE")
    @allure.title('Allure Title')
    @allure.description('Allure Description')
    def test_login_sales(self):
        self.lo = LoginPage(self.driver)
        self.lo.get_url(ReadConfig_URL.SET_ADMIN_URL(), "URL Entered")
        self.lo.enter_username(ReadConfig_LOGIN.SET_LOGIN_EMAIL4(), "Admin Username")
        self.lo.enter_password(ReadConfig_LOGIN.SET_LOGIN_PASSWORD4(), "Admin password")
        self.lo.enter_click("Login Button Click")