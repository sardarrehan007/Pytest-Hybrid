from Librariries import *
from Main.ConfigReader import ReadConfig_URL, ReadConfig_LOGIN
from PageObject.LoginPage import LoginPage
from Tests.test_BaseTest import BaseTest
import sys
sys.setrecursionlimit(10000)

class Test_Login(BaseTest):

    @allure.feature("SUITE")
    @allure.title('Allure Title')
    @allure.description('Allure Description')
    def test_login_01(self):
        self.lp1 = LoginPage(self.driver)
        self.lp1.get_url(ReadConfig_URL.SET_ADMIN_URL(), "URL Entered")
        self.lp1.enter_username(ReadConfig_LOGIN.SET_LOGIN_EMAIL(), "Admin Username")
        self.lp1.enter_password(ReadConfig_LOGIN.SET_LOGIN_PASSWORD(), "Admin password")
        self.lp1.enter_click("Login Button Click")

