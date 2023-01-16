from Librariries import *
from Main.ConfigReader import ReadConfig_URL, ReadConfig_LOGIN
from PageObject.Lab_Page import LabPage
from Tests.test_BaseTest import BaseTest

import sys
sys.setrecursionlimit(10000)

class Test_LabScenario(BaseTest):
    @allure.feature("SUITE")
    @allure.title('Allure Title')
    @allure.description('Allure Description')

    def test_labscenario2(self):
        self.lp= LabPage(self.driver)
        self.lp.Click_Pending_Receivable("okokok")
        self.lp.Click_Create_new_memo("fhjvc")
        self.lp.Click_vendor('r', "ghvhvv")
        self.lp.Click_Submit_Button("vcjhdvc")
        self.lp.Click_Pending_memo("loll")
        self.lp.Click_Received_memo("klklklk")
        self.lp.Click_Sure_memo("kklklklk")

        #self.lp.Click_Create_new_memo("fhjvc")
        ##self.lp.Click_vendor('r',"ghvhvv")
        #self.lp.Click_Submit_Button("vcjhdvc")
        self.lp.Click_Add_Stone("jbsdc")
        time.sleep(5)
        self.lp.Click_Stone_type('H',"jbcbdc")
        self.lp.Enter_no_of_stones('1',"clkad")
        self.lp.Enter_submit_button("jabjz")
        self.lp.Click_Received_memo("klklklk")
        self.lp.Click_Sure_memo("kklklklk")
        time.sleep(5)
        self.lp.Click_Received_memo("klklklk")
        self.lp.Click_Sure_memo("kklklklk")

        self.lp.Click_Pending_Data("ggjg")

        self.lp.Click_Data_done("ggbigkgi")
        self.lp.Click_Stone_Type('R',"kulak")


        self.lp.Enter_weight('10',"kskskk")
        time.sleep(6)

        self.lp.Click_Shape('oval',"jkj")
        self.lp.Enter_Measurement('10.5',"hhjhj")
        time.sleep(11)
        self.lp.Enter_Measurement2('7',"hih")
        time.sleep(11)

        self.lp.Enter_Measurement3('8',"kjjkjkj")
        time.sleep(11)


        self.lp.Click_Stone_cut('Brilliant',"dcsd")
        time.sleep(11)


        self.lp.Click_origin('B', "dcsd")
        time.sleep(11)


        self.lp.Click_Traceable_origin('n',"hsfkhsdjf")
        time.sleep(11)


        self.lp.Click_Treatment_now('h',"jdsbhdkgvj")
        time.sleep(11)

        #time.sleep(6)
        #self.lp.is_scroll_in_position("0", "800", "scroll")

        self.lp.Click_species('n',"gjvjhv")
        time.sleep(11)

        self.lp.Click_varieties('a',"Click_varieties")
        time.sleep(11)

        self.lp.Click_Color('bi',"gggh")
        time.sleep(11)

        self.lp.Click_intensity('d', "jbkjb")
        time.sleep(11)

        self.lp.Click_clarity('e', "jnn")
        time.sleep(5)
        #self.lp.is_scroll_in_position("0", "1600", "scroll")

        self.lp.Click_polish_dd("Cut Grade")
        self.lp.Click_symmetry_dd("Cut Grade")
        self.lp.Click_proportion_dd("Cut Grade")
        #self.lp.Cut_grade_standard("smkmx ")
        time.sleep(5)





        #self.lp.Click_Images("gbkdfnbk")
        time.sleep(5)



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
        #self.lp.Click_Table_ref_num("c")





        time.sleep(5)
