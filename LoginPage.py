from selenium.webdriver.common.by import By

from Librariries import *
from DataDriven import TestData
from Main.CorePage import CorePage


class LoginPage(CorePage):
    username_Id = TestData.jsonlogin_id_r["LoginPage"]["textbox_username"]
    password_Id = TestData.jsonlogin_id_r["LoginPage"]["textbox_password"]
    LoginBtn_Id = TestData.jsonlogin_id_r["LoginPage"]["btn_login"]

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username, allure_Screenshot_name):
        self.do_enter_text((By.XPATH, self.username_Id), username, allure_Screenshot_name)

    def enter_password(self, password, allure_Screenshot_name):
        self.do_enter_text((By.XPATH, self.password_Id), password, allure_Screenshot_name)

    def enter_click(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.LoginBtn_Id), allure_Screenshot_name)
