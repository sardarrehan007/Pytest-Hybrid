from Librariries import *
from PageObject.Newsplit_Page import NewSplitPage
from PageObject.Split_Page import SplitPage
from Tests.test_BaseTest import BaseTest

class Test_Split1(BaseTest):
    @allure.feature("SUITE")
    @allure.title('Allure Title')
    @allure.description('Allure Description')
    def test_split(self):
        self.sp = NewSplitPage(self.driver)
        self.sp.Click_Catalog("gem catalog")
        time.sleep(5)
        self.sp.Click_My_Inventory("gem catalog")
        time.sleep(5)
        self.sp.Click_Checkbox("ajbc")
        time.sleep(3)

        self.sp.Enter_Split_Button("bdbj")
        time.sleep(10)

        self.sp.Click_num_of_stones('1',"P")

        self.sp.Click_gem_Add("CSDSDCSC")
        self.sp.Check_split_type("hskdjba")
        #self.sp.is_scroll_in_position('0','900',"ddds")
        #self.sp.Click_submit("bdbc")
        #self.sp.Click_Close_split("nadkjfb")

        time.sleep(5)
