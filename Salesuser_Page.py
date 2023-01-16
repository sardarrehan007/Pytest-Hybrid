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
    stone_inventory_sales = TestData.json_lab["Lab"]["stone_inventory_sales"]
    Click_Grid_view=TestData.json_lab["Lab"]["Grid_view"]
    stone_type=TestData.json_lab["Lab"]["stone_type"]
    Enter_Stone_type=TestData.json_lab["Lab"]["Enter_Stone_type"]
    color = TestData.json_lab["Lab"]["color"]
    Enter_color = TestData.json_lab["Lab"]["Enter_Color"]
    clarity = TestData.json_lab["Lab"]["Clarity"]
    enter_clarity = TestData.json_lab["Lab"]["Enter_Clarity"]
    Intensity = TestData.json_lab["Lab"]["intensity"]
    Enter_intensity = TestData.json_lab["Lab"]["Enter_Intensity"]
    Apply_Filter=TestData.json_lab["Lab"]["Apply_Filter"]
    Select_stone=TestData.json_lab["Lab"]["Select_stone"]


    def __init__(self, driver):
        super().__init__(driver)

    def Click_stone_inventory_sales(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.stone_inventory_sales), allure_Screenshot_name)

    def Grid_view(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.Click_Grid_view), allure_Screenshot_name)
    def Click_stone_type(self,Text, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.stone_type), allure_Screenshot_name)
        self.do_enter_text((By.CSS_SELECTOR, self.Enter_Stone_type), Text, allure_Screenshot_name)
        self.do_press_enter((By.CSS_SELECTOR, self.Enter_Stone_type), allure_Screenshot_name)
    def Click_color(self,Text, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.color), allure_Screenshot_name)
        self.do_enter_text((By.CSS_SELECTOR, self.Enter_color), Text, allure_Screenshot_name)
        self.do_press_enter((By.CSS_SELECTOR, self.Enter_color), allure_Screenshot_name)

    def Click_intensity(self,Text, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.Intensity), allure_Screenshot_name)
        self.do_enter_text((By.CSS_SELECTOR, self.Enter_intensity), Text, allure_Screenshot_name)
        self.do_press_enter((By.CSS_SELECTOR, self.Enter_intensity), allure_Screenshot_name)
        self.do_click((By.CSS_SELECTOR, self.Intensity), allure_Screenshot_name)

    def Click_clarity(self,Text, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.clarity), allure_Screenshot_name)
        self.do_enter_text((By.CSS_SELECTOR, self.enter_clarity), Text, allure_Screenshot_name)
        self.do_press_enter((By.CSS_SELECTOR, self.enter_clarity), allure_Screenshot_name)
        self.do_click((By.CSS_SELECTOR, self.clarity), allure_Screenshot_name)

    def Click_Apply_Filter(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.Apply_Filter), allure_Screenshot_name)
    def Click_Select_stone(self, allure_Screenshot_name):
        self.do_click((By.ID, self.Select_stone), allure_Screenshot_name)

