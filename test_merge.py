from Librariries import *
from PageObject.merge import MergePage
from Tests.test_BaseTest import BaseTest

class Test_Merge(BaseTest):
    @allure.feature("SUITE")
    @allure.title('Allure Title')
    @allure.description('Allure Description')


    def test_merge(self):
      self.m1 = MergePage(self.driver)
      self.m1.Click_Catalog("gem catalog")
      self.m1.Click_My_Inventory("my inventory")
      self.m1.Select_Stone1("gem catalog")
      time.sleep(5)
