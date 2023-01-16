
from DataDriven import TestData
from Librariries import *
from Main.CorePage import CorePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def send_keys(param):
    pass


def key_down(Control):
    pass


class SupplierMemoPage(CorePage):
    Accounting_Supply=TestData.json_dashboard_r["Dashboard"]["Accounting_Supply"]
    Select_memo=TestData.json_dashboard_r["Dashboard"]["Select_memo"]
    supplier_memo1=TestData.json_dashboard_r["Dashboard"]["Select_supplier_memo1"]
    CreateMemo=TestData.json_dashboard_r["Dashboard"]["CreateMemo"]
    add_more_stones=TestData.json_dashboard_r["Dashboard"]["add_more_stones"]
    merge_checkbox1=TestData.json_dashboard_r["Dashboard"]["merge_checkbox1"]
    click_header_memo=TestData.json_dashboard_r["Dashboard"]["click_header_memo"]



    def __init__(self, driver):
        super().__init__(driver)
    def Click_Accounting(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.Accounting_Supply), allure_Screenshot_name)
    def Click_memo(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.Select_memo), allure_Screenshot_name)
    def Select_supplier_memo1(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.supplier_memo1), allure_Screenshot_name)
    def Click_CreateMemo(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.CreateMemo), allure_Screenshot_name)
    def Click_add_more_stones(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.add_more_stones), allure_Screenshot_name)
    def Click_Checkbox(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.merge_checkbox1), allure_Screenshot_name)
    def Click_header_memo(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.click_header_memo), allure_Screenshot_name)

