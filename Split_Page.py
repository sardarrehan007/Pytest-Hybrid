from DataDriven import TestData
from Librariries import *
from Main.CorePage import CorePage


def send_keys(param):
    pass


class SplitPage(CorePage):
    Production = TestData.json_dashboard_r["Dashboard"]["Production"]
    Work_in_process= TestData.json_dashboard_r["Dashboard"]["Work_in_process"]
    internal_click=TestData.json_dashboard_r["Dashboard"]["internal_click"]
    num_of_stones=TestData.json_dashboard_r["Dashboard"]["no_of_stones"]
    add_gem_Stone_split = TestData.json_dashboard_r["Dashboard"]["add_gem_Stone_split"]
    Close_split = TestData.json_dashboard_r["Dashboard"]["Close_split"]
    Select_split_type=TestData.json_dashboard_r["Dashboard"]["Select_split type"]
    Regular=TestData.json_dashboard_r["Dashboard"]["Regular"]
    submit=TestData.json_dashboard_r["Dashboard"]["submit"]
    def __init__(self, driver):
          super().__init__(driver)

    def Click_production(self, allure_Screenshot_name):
       self.do_click((By.XPATH, self.Production), allure_Screenshot_name)
    def Click_Work_in_process1(self, allure_Screenshot_name):
       self.do_click((By.XPATH, self.Work_in_process), allure_Screenshot_name)
    def Click_internal_click(self, allure_Screenshot_name):
       self.do_click((By.XPATH, self.internal_click), allure_Screenshot_name)

    def Click_num_of_stones(self, Numeric_value, allure_Screenshot_name):
       self.do_click((By.ID, self.num_of_stones), allure_Screenshot_name)
       self.do_enter_text((By.ID, self.num_of_stones),Numeric_value, allure_Screenshot_name)
       self.do_press_enter((By.ID, self.num_of_stones), allure_Screenshot_name)
    def Click_gem_Add(self, allure_Screenshot_name):
       self.do_click((By.XPATH, self.add_gem_Stone_split), allure_Screenshot_name)


    def Click_Close_split(self, allure_Screenshot_name):
       self.do_click((By.CSS_SELECTOR, self.Close_split), allure_Screenshot_name)
    def Check_split_type(self, allure_Screenshot_name):
       self.do_click((By.CSS_SELECTOR, self.Select_split_type), allure_Screenshot_name)
       self.do_click((By.CSS_SELECTOR, self.Regular), allure_Screenshot_name)
    def Click_submit(self, allure_Screenshot_name):
       self.do_click((By.CSS_SELECTOR, self.Close_split), allure_Screenshot_name)











































































