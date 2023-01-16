import self as self

from DataDriven import TestData
from Librariries import *
from Main.CorePage import CorePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def send_keys(param):
    pass


def key_down(Control):
    pass


class SalesPage(CorePage):
    sale_inventory=TestData.json_sales["Sales"]["sale_inventory"]
    check_salestone=TestData.json_sales["Sales"]["check_salestone"]
    select_list=TestData.json_sales["Sales"]["select_list"]
    select_all=TestData.json_sales["Sales"]["select_all"]
    convert_to_sales=TestData.json_sales["Sales"]["convert_to_sales"]
    choose_api_user=TestData.json_sales["Sales"]["choose_api_user"]
    gemolith=TestData.json_sales["Sales"]["gemolith"]
    choose_memo_terms=TestData.json_sales["Sales"]["choose_memo_terms"]
    select_terms = TestData.json_sales["Sales"]["select_terms"]
    saveandclose=TestData.json_sales["Sales"]["saveandclose"]
    def __init__(self, driver):
        super().__init__(driver)
    def Click_Stone_inventory(self, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.sale_inventory),allure_Screenshot_name)

    def Click_check_salestone(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.check_salestone), allure_Screenshot_name)
    def Click_select_list(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.select_list), allure_Screenshot_name)
    def Click_select_all(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.select_all), allure_Screenshot_name)
    def Click_convert_to_sales(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.convert_to_sales), allure_Screenshot_name)
    def Click_choose_api_user(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.choose_api_user), allure_Screenshot_name)
        self.do_click((By.CSS_SELECTOR, self.gemolith), allure_Screenshot_name)

    def Click_choose_memo_terms(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.choose_memo_terms), allure_Screenshot_name)
        self.do_click((By.CSS_SELECTOR, self.select_terms), allure_Screenshot_name)
    def Click_saveandclose(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.saveandclose), allure_Screenshot_name)







