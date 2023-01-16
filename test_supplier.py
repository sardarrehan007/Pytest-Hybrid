from Tests.test_BaseTest import BaseTest
from Librariries import *
from PageObject.SupplierMemo_Page import SupplierMemoPage

class Test_SupplierMemo(BaseTest):

    @allure.feature("SUITE")
    @allure.title('Allure Title')
    @allure.description('Allure Description')


    def test_suppliermemo(self):
        self.sm =SupplierMemoPage(self.driver)
        self.sm.Click_Accounting("nknknkn")
        self.sm.Click_memo("bdbd")
        time.sleep(5)
        self.sm.Select_supplier_memo1("djududn")
        self.sm.Click_CreateMemo("cddcd")
        self.sm.Click_add_more_stones("nsnjcn")
        self.sm.Click_Checkbox("fff")
        self.sm.Click_header_memo("jdjd")
        time.sleep(5)