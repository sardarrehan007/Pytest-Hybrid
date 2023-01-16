from Librariries import *
from Main.ConfigReader import ReadConfig_URL, ReadConfig_LOGIN
from PageObject.Lab_Page import LabPage
from Tests.test_BaseTest import BaseTest

import sys
sys.setrecursionlimit(10000)

class Test_LabScenario00(BaseTest):
    @allure.feature("SUITE")
    @allure.title('Allure Title')
    @allure.description('Allure Description')

    def test_labscenario00(self):
        self.lp= LabPage(self.driver)
        self.lp.Click_Pending_Receivable("okokok")
        self.lp.Click_Pending_memo("loll")
        self.lp.Click_Received_memo("klklklk")

        self.lp.Click_Sure_memo("kklklklk")

        self.lp.Click_Pending_Data("ggjg")

        self.lp.Click_Data_done("ggbigkgi")
        self.lp.Click_Stone_Type('R',"kulak")


        self.lp.Enter_weight('10',"kskskk")
        time.sleep(6)

        self.lp.Click_Shape('oval',"jkj")
        self.lp.Enter_Measurement('10.5',"hhjhj")
        self.lp.Enter_Measurement2('7',"hih")
        self.lp.Enter_Measurement3('8',"kjjkjkj")

        self.lp.Click_Stone_cut('Brilliant',"dcsd")

        self.lp.Click_origin('B', "dcsd")

        self.lp.Click_Traceable_origin('n',"hsfkhsdjf")

        self.lp.Click_Treatment_now('h',"jdsbhdkgvj")
        #time.sleep(6)
        #self.lp.is_scroll_in_position("0", "800", "scroll")



        #self.lp.Click_Images("gbkdfnbk")
        time.sleep(5)



        self.lp.is_scroll_in_position("679", "1960", "scroll")
        self.lp.Click_save("';;';';")
        self.lp.Click_yes_Button("kxbksab")

        self.lp.Click_Pending_QC("gvgv")
        self.lp.Click_QC("kjskbdc")
        self.lp.Click_Sure_QC("cc")
        self.lp.Click_Close_Manager("jjsh")
        self.lp.Click_Manager("manager")
        self.lp.Click_Yes_Manager("khcjdhvc")

