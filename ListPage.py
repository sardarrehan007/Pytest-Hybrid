from DataDriven import TestData
from Librariries import *
from Main.CorePage import CorePage


def send_keys(param):
    pass


class ListPage(CorePage):
    gem_stone_catalog = TestData.json_dashboard_r["Dashboard"]["Gemstone_Catalog_xpath"]
    my_inventory = TestData.json_dashboard_r["Dashboard"]["My_inventory_xpath"]
    merge_checkbox1 = TestData.json_dashboard_r["Dashboard"]["merge_checkbox1"]
    merge_checkbox2 = TestData.json_dashboard_r["Dashboard"]["merge_checkbox2"]
    List = TestData.json_dashboard_r["Dashboard"]["List"]

    def __init__(self, driver):
        super().__init__(driver)

    def Click_Catalog(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.gem_stone_catalog), allure_Screenshot_name)

    def Click_My_Inventory(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.my_inventory), allure_Screenshot_name)

    def Select_Stone1(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.merge_checkbox1), allure_Screenshot_name)
        self.do_click((By.XPATH, self.merge_checkbox2), allure_Screenshot_name)

    def Click_List(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.List), allure_Screenshot_name)
