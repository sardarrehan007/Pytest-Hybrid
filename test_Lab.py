from Librariries import *
from PageObject.Lab_Page import LabPage
from Tests.test_BaseTest import BaseTest

import sys
sys.setrecursionlimit(10000)

class Test_Lab(BaseTest):
    @allure.feature("SUITE")
    @allure.title('Allure Title')
    @allure.description('Allure Description')

    def test_lab(self):
        self.lp = LabPage(self.driver)
        self.lp.Click_Pending_Receivable("okokok")
        self.lp.Click_Pending_memo("loll")
        self.lp.Click_Received_memo("klklklk")

        self.lp.Click_Sure_memo("kklklklk")

        self.lp.Click_Pending_Data("ggjg")

        self.lp.Click_Data_done("ggbigkgi")
        #self.lp.Click_Stone_Type('R',"kulak")

        self.lp.is_scroll_in_position("679", "1960", "scroll")
        self.lp.Click_save("';;';';")
        self.lp.Click_yes_Button("kxbksab")
        self.lp.Click_Pending_QC("djb")
        #self.lp.data_entry_done("hhb")
        #self.lp.Click_save("';;';';")
        #self.lp.Click_yes_Button("kxbksab")
        self.lp.Click_QC("gvgv")
        self.lp.Click_Sure_QC("cc")
        self.lp.Click_Close_Manager("jjsh")
        self.lp.Click_Manager("manager")
        self.lp.Click_Yes_Manager("khcjdhvc")
        time.sleep(7)
        self.Click_Table_ref_num("hfjh")
        time.sleep(6)

        time.sleep(5)
