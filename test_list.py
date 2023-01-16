from Librariries import *
from PageObject.ListPage import ListPage
from Tests.test_BaseTest import BaseTest



class Test_List(BaseTest):
    @allure.feature("SUITE")
    @allure.title('Allure Title')
    @allure.description('Allure Description')


    def test_list(self):
        self.l1 = ListPage(self.driver)
        self.l1.Click_Catalog("gem catalog")
        self.l1.Click_My_Inventory("my inventory")
        self.l1.Select_Stone1("gem catalog")
        self.l1.Click_List("FSFDS")