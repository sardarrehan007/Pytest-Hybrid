from Librariries import *
from PageObject.Dashboard_Page import DashboardPage
from Tests.test_BaseTest import BaseTest


class Test_Split(BaseTest):

    def test_dashboard(self):
        self.lp1 = DashboardPage(self.driver)
        self.lp1.Click_Catalog("gem catalog")
        self.lp1.Click_My_Inventory("my inventory")
