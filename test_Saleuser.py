from Librariries import *
from PageObject.Salesuser_Page import SalesPage
from PageObject.merge import MergePage
from Tests.test_BaseTest import BaseTest
from PageObject.Sales_Page import SalesPage

class Test_Salesuser(BaseTest):
    @allure.feature("SUITE")
    @allure.title('Allure Title')
    @allure.description('Allure Description')
    def test_sales(self):
        self.sp = SalesPage(self.driver)
        self.sp.Click_Stone_inventory("hhjhj")
        self.sp.Click_check_salestone("uguggg")
        self.sp.Click_select_list("ug")
        self.sp.Click_select_all("ug")
        self.sp.Click_convert_to_sales("yygyg")
        self.sp.Click_choose_api_user("jhf")
        self.sp.Click_choose_memo_terms("fg")
        self.sp.Click_saveandclose("yuyf")
        time.sleep(10)

