from Librariries import *
from Main.ConfigReader import ReadConfig_URL, ReadConfig_LOGIN
from PageObject.Lab_Page import LabPage
from PageObject.Ops_Page import OpsPage
from Tests.test_BaseTest import BaseTest

import sys
sys.setrecursionlimit(10000)

class Test_Ops(BaseTest):
    @allure.feature("SUITE")
    @allure.title('Allure Title')
    @allure.description('Allure Description')

    def test_ops(self):
        self.op= OpsPage(self.driver)
        time.sleep(5)
        self.op.Click_verified_stones("jkkjkj")
        time.sleep(8)