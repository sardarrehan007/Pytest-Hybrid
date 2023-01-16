from DataDriven import TestData
from Librariries import *
from Main.CorePage import CorePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def send_keys(param):
    pass


class OpsPage(CorePage):
    verified_stones = TestData.json_lab["Lab"]["verified_stones"]
    def __init__(self, driver):
        super().__init__(driver)

    def Click_verified_stones(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.verified_stones), allure_Screenshot_name)