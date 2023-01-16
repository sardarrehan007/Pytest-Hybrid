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


class NewSplitPage(CorePage):
    Gemstone_Catalog_xpath=TestData.json_dashboard_r["Dashboard"]["Gemstone_Catalog_xpath"]
    My_inventory_xpath=TestData.json_dashboard_r["Dashboard"]["My_inventory_xpath"]
    merge_checkbox1=TestData.json_dashboard_r["Dashboard"]["merge_checkbox1"]
    merge_checkbox2=TestData.json_dashboard_r["Dashboard"]["merge_checkbox2"]
    click_split=TestData.json_dashboard_r["Dashboard"]["Enter_Split_Button"]
    num_of_stones=TestData.json_dashboard_r["Dashboard"]["no_of_stones"]
    add_gem_Stone_split=TestData.json_dashboard_r["Dashboard"]["add_gem_Stone_split"]
    Select_split=TestData.json_dashboard_r["Dashboard"]["Select_split type"]
    Regular=TestData.json_dashboard_r["Dashboard"]["Regular"]
    def __init__(self, driver):
        super().__init__(driver)
    def Click_Catalog(self, allure_Screenshot_name):
         self.do_click((By.ID, self.Gemstone_Catalog_xpath),allure_Screenshot_name)

    def Click_My_Inventory(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.My_inventory_xpath), allure_Screenshot_name)
    def Click_Checkbox(self, allure_Screenshot_name):
         self.do_click((By.XPATH, self.merge_checkbox1),allure_Screenshot_name)

        #self.do_click((By.XPATH, self.merge_checkbox2), allure_Screenshot_name)

    def Enter_Split_Button(self, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.click_split),allure_Screenshot_name)

    def Click_num_of_stones(self, Numeric_value, allure_Screenshot_name):
       self.do_click((By.ID, self.num_of_stones), allure_Screenshot_name)
       self.do_enter_text((By.ID, self.num_of_stones),Numeric_value, allure_Screenshot_name)
       self.do_press_enter((By.ID, self.num_of_stones), allure_Screenshot_name)
    def Click_gem_Add(self, allure_Screenshot_name):
       self.do_click((By.XPATH, self.add_gem_Stone_split), allure_Screenshot_name)

    def Check_split_type(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.Select_split), allure_Screenshot_name)
        self.do_click((By.CSS_SELECTOR, self.Regular), allure_Screenshot_name)

