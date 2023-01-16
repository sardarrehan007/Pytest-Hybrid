import self as self

from DataDriven import TestData
from Librariries import *
from Main.CorePage import CorePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def send_keys(param):
    pass


def key_down(Control):
    pass


class LabPage(CorePage):
    Pending_Receiveables=TestData.json_lab["Lab"]["Pending_Receiveables"]
    Pending_Receivable_memos=TestData.json_lab["Lab"]["Pending_Receivable_memos"]

    Received_memo=TestData.json_lab["Lab"]["Memo_Received"]
    Sure_memo=TestData.json_lab["Lab"]["Sure_memo"]
    Pending_Data=TestData.json_lab["Lab"]["Pending_data"]
    Data_done=TestData.json_lab["Lab"]["Data_Done"]
    save_Data=TestData.json_lab["Lab"]["save"]
    Pending_QC=TestData.json_lab["Lab"]["Pending_QC"]
    Click_yes=TestData.json_lab["Lab"]["Click_Yes"]
    data_entry_done=TestData.json_lab["Lab"]["data_entry_done"]
    close_qc=TestData.json_lab["Lab"]["close_qc"]
    Sure_QC=TestData.json_lab["Lab"]["Sure_QC"]
    Manager=TestData.json_lab["Lab"]["Manager"]
    Close_Manager=TestData.json_lab["Lab"]["Close_Manager"]
    Yes_Manager = TestData.json_lab["Lab"]["Click_Yes_Manager"]
    Stone_Type=TestData.json_lab["Lab"]["Stone_Type"]
    Enter_Text=TestData.json_lab["Lab"]["Enter_Stone"]
    weight=TestData.json_lab["Lab"]["weight"]
    Cut_type=TestData.json_lab["Lab"]["Cut_type"]
    Enter_cut=TestData.json_lab["Lab"]["Enter_cut"]
    M1=TestData.json_lab["Lab"]["Measurement"]
    M2=TestData.json_lab["Lab"]["Measurement2"]
    M3=TestData.json_lab["Lab"]["Measurement3"]
    Stone_cut=TestData.json_lab["Lab"]["Stone_cut"]
    Enter_Stonecut=TestData.json_lab["Lab"]["Enter_Stonecut"]
    Origin=TestData.json_lab["Lab"]["origin"]
    Enter_origin=TestData.json_lab["Lab"]["enter_origin"]
    Traceable_Origin=TestData.json_lab["Lab"]["Traceable_Origin"]
    Enter_Traceable=TestData.json_lab["Lab"]["Enter_Traceable"]
    Treatment=TestData.json_lab["Lab"]["Treatment"]
    Enter_Treatment=TestData.json_lab["Lab"]["Enter_Treatment"]
    images=TestData.json_lab["Lab"]["360_images"]
    Upload=TestData.json_lab["Lab"]["upload"]
    Species=TestData.json_lab["Lab"]["Species"]
    Enter_Species=TestData.json_lab["Lab"]["Enter_Species"]
    Color=TestData.json_lab["Lab"]["colors"]
    Enter_color=TestData.json_lab["Lab"]["enter_color"]
    Varieties=TestData.json_lab["Lab"]["varities"]
    enter_varieties=TestData.json_lab["Lab"]["enter_varieties"]
    clarity=TestData.json_lab["Lab"]["clarity"]
    enter_clarity=TestData.json_lab["Lab"]["enter_clarity"]
    Intensity=TestData.json_lab["Lab"]["Intensity"]
    Enter_intensity=TestData.json_lab["Lab"]["enter_intensity"]
    polish=TestData.json_lab["Lab"]["Polish"]
    select_polish = TestData.json_lab["Lab"]["Select_Polish"]
    symmetry = TestData.json_lab["Lab"]["Symmetry"]
    select_symmetry = TestData.json_lab["Lab"]["Select_Symmetry"]
    proportion = TestData.json_lab["Lab"]["Proportion"]
    select_proportion = TestData.json_lab["Lab"]["Select_Proportion"]
    click_ref=TestData.json_lab["Lab"]["click_ref"]
    logout=TestData.json_lab["Lab"]["logout"]
    Click_logout_lab=TestData.json_lab["Lab"]["Click_logout_lab"]
    verified_stones=TestData.json_lab["Lab"]["verified_stones"]
    cut_grade_standard=TestData.json_lab["Lab"]["cut_grade_standard"]
    Table_ref_num=TestData.json_lab["Lab"]["Table_ref_num"]
    Create_memo=TestData.json_lab["Lab"]["Create_memo_lab"]
    Click_Vendor=TestData.json_lab["Lab"]["Click_Vendor"]
    Enter_Vendor=TestData.json_lab["Lab"]["Enter_Vendor"]
    Click_Submit=TestData.json_lab["Lab"]["Click_Submit"]
    Add_Stone=TestData.json_lab["Lab"]["Add_Stone"]
    Stone_type=TestData.json_lab["Lab"]["Stone_type"]
    Enter_Stones=TestData.json_lab["Lab"]["Enter_Stones"]
    no_of_stones=TestData.json_lab["Lab"]["no_of_stones"]
    submit_button=TestData.json_lab["Lab"]["submit_button"]

    def __init__(self, driver):
        super().__init__(driver)
    def Click_Pending_Receivable(self, allure_Screenshot_name):
         self.do_click((By.XPATH, self.Pending_Receiveables),allure_Screenshot_name)
    def  Click_Pending_memo(self, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.Pending_Receivable_memos),allure_Screenshot_name)
    def  Click_Received_memo(self, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.Received_memo),allure_Screenshot_name)
    def  Click_Sure_memo(self, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.Sure_memo),allure_Screenshot_name)
    def  Click_Pending_Data(self, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.Pending_Data),allure_Screenshot_name)
    def  Click_Data_done(self, allure_Screenshot_name):
         self.do_click((By.XPATH, self.Data_done),allure_Screenshot_name)
    def  Click_save(self, allure_Screenshot_name):
     #self.is_scroll_in_position(self.)
         self.do_click((By.ID, self.save_Data),allure_Screenshot_name)
    def  Click_Pending_QC(self, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.Pending_QC),allure_Screenshot_name)
    def Click_yes_Button(self, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.Click_yes),allure_Screenshot_name)
    def Data_entry_done(self, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.data_entry_done),allure_Screenshot_name)
    def Click_QC(self, allure_Screenshot_name):
         self.do_click((By.ID, self.close_qc),allure_Screenshot_name)
    def Click_Sure_QC(self, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.Sure_QC),allure_Screenshot_name)
    def Click_Manager(self, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.Manager),allure_Screenshot_name)
    def Click_Close_Manager(self, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.Close_Manager),allure_Screenshot_name)
    def Click_Yes_Manager(self, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.Yes_Manager),allure_Screenshot_name)
    def Click_Stone_Type(self, Text, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.Stone_Type), allure_Screenshot_name)
         self.do_enter_text((By.CSS_SELECTOR, self.Enter_Text),Text, allure_Screenshot_name)
         self.do_press_enter((By.CSS_SELECTOR, self.Enter_Text), allure_Screenshot_name)
    def Enter_weight(self, Numeric_value, allure_Screenshot_name):
         #self.do_click((By.XPATH, self.Stone_Type), allure_Screenshot_name)
         self.do_enter_text((By.ID, self.weight),Numeric_value, allure_Screenshot_name)
         self.do_press_enter((By.ID, self.weight), allure_Screenshot_name)
    def Click_Shape(self, Text, allure_Screenshot_name):
         self.do_click((By.ID, self.Cut_type), allure_Screenshot_name)
         self.do_enter_text((By.CSS_SELECTOR, self.Enter_cut),Text, allure_Screenshot_name)
         self.do_press_enter((By.CSS_SELECTOR, self.Enter_cut), allure_Screenshot_name)

    def Enter_Measurement(self, Numeric_value, allure_Screenshot_name):
         #self.do_click((By.XPATH, self.Stone_Type), allure_Screenshot_name)
         self.do_enter_text((By.CSS_SELECTOR, self.M1),Numeric_value, allure_Screenshot_name)
         self.do_press_enter((By.CSS_SELECTOR, self.M1), allure_Screenshot_name)

    def Enter_Measurement2(self, Numeric_value, allure_Screenshot_name):
         self.do_enter_text((By.CSS_SELECTOR, self.M2), Numeric_value, allure_Screenshot_name)
         self.do_press_enter((By.CSS_SELECTOR, self.M2), allure_Screenshot_name)

    def Enter_Measurement3(self, Numeric_value, allure_Screenshot_name):
         self.do_enter_text((By.CSS_SELECTOR, self.M3), Numeric_value, allure_Screenshot_name)
         self.do_press_enter((By.CSS_SELECTOR, self.M3), allure_Screenshot_name)
    def Click_Stone_cut(self, Text, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.Stone_cut), allure_Screenshot_name)
         self.do_enter_text((By.CSS_SELECTOR, self.Enter_Stonecut),Text, allure_Screenshot_name)
         self.do_press_enter((By.CSS_SELECTOR, self.Enter_Stonecut), allure_Screenshot_name)
    def Click_origin(self, Text, allure_Screenshot_name):
         self.do_click((By.ID, self.Origin), allure_Screenshot_name)
         self.do_enter_text((By.CSS_SELECTOR, self.Enter_origin),Text, allure_Screenshot_name)
         self.do_press_enter((By.CSS_SELECTOR, self.Enter_origin), allure_Screenshot_name)
    def Click_Traceable_origin(self, Text, allure_Screenshot_name):
         self.do_click((By.CSS_SELECTOR, self.Traceable_Origin), allure_Screenshot_name)
         self.do_enter_text((By.CSS_SELECTOR, self.Enter_Traceable),Text, allure_Screenshot_name)
         self.do_press_enter((By.CSS_SELECTOR, self.Enter_Traceable), allure_Screenshot_name)

    def Click_Treatment_now(self, Text, allure_Screenshot_name):
         self.do_click((By.ID, self.Treatment), allure_Screenshot_name)
         self.do_enter_text((By.CSS_SELECTOR, self.Enter_Treatment), Text, allure_Screenshot_name)
         self.do_press_enter((By.CSS_SELECTOR, self.Enter_Treatment), allure_Screenshot_name)
    def Click_Images(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.images), allure_Screenshot_name)
        self.do_click((By.ID, self.Upload), allure_Screenshot_name)
       # self.get_upload_file_with_path((By.ID, self.images), path, allure_Screenshot_name)
    def Click_dropdown_value1(self, allure_Screenshot_name):
        self.do_dropdown_by_value((By.CSS_SELECTOR, "/body > div.wrapper.justify-content-between > div > div.right-content.justify-content-between > div.row.entriestable-row.mt-3 > div > div > div > div > div.col-7.stone-detail-tablr.mb-5.pb-5 > table:nth-child(3) > tbody > tr:nth-child(6) > td:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(1) > select"), "3", allure_Screenshot_name)
    def Click_species(self, Text, allure_Screenshot_name):
         self.do_click((By.ID, self.Species), allure_Screenshot_name)
         self.do_enter_text((By.CSS_SELECTOR, self.Enter_Species),Text, allure_Screenshot_name)
         self.do_press_enter((By.CSS_SELECTOR, self.Enter_Species), allure_Screenshot_name)
    def Click_varieties(self, Text, allure_Screenshot_name):
         self.do_click((By.ID, self.Varieties), allure_Screenshot_name)
         self.do_enter_text((By.CSS_SELECTOR, self.enter_varieties),Text, allure_Screenshot_name)
         self.do_press_enter((By.CSS_SELECTOR, self.enter_varieties), allure_Screenshot_name)
    def Click_Color(self, Text, allure_Screenshot_name):
         self.do_click((By.ID, self.Color), allure_Screenshot_name)
         self.do_enter_text((By.CSS_SELECTOR, self.Enter_color),Text, allure_Screenshot_name)
         self.do_press_enter((By.CSS_SELECTOR, self.Enter_color), allure_Screenshot_name)

    def Click_clarity(self, Text, allure_Screenshot_name):
        self.do_click((By.ID, self.clarity), allure_Screenshot_name)
        self.do_enter_text((By.CSS_SELECTOR, self.enter_clarity), Text, allure_Screenshot_name)
        self.do_press_enter((By.CSS_SELECTOR, self.enter_clarity), allure_Screenshot_name)

    def Click_intensity(self, Text, allure_Screenshot_name):
        self.do_click((By.ID, self.Intensity), allure_Screenshot_name)
        self.do_enter_text((By.CSS_SELECTOR, self.Enter_intensity), Text, allure_Screenshot_name)
        self.do_press_enter((By.CSS_SELECTOR, self.Enter_intensity), allure_Screenshot_name)

    def Click_polish_dd(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.polish), allure_Screenshot_name)
        self.do_click((By.CSS_SELECTOR, self.select_polish), allure_Screenshot_name)

    def Click_symmetry_dd(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.symmetry), allure_Screenshot_name)
        self.do_click((By.CSS_SELECTOR, self.select_symmetry), allure_Screenshot_name)

    def Click_proportion_dd(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.proportion), allure_Screenshot_name)
        self.do_click((By.CSS_SELECTOR, self.select_proportion), allure_Screenshot_name)
    def Click_Ref(self, allure_Screenshot_name,allure_controlKeydown_screenshot_name):
        self.do_double_click((By.XPATH, self.click_ref), allure_Screenshot_name)
        self.get_control_Keydown_actions((self, 'c'), allure_controlKeydown_screenshot_name)
    def Click_Log(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.logout), allure_Screenshot_name)
        self.do_click((By.CSS_SELECTOR, self.Click_logout_lab), allure_Screenshot_name)
    def Cut_grade_standard(self, allure_Screenshot_name):
        self.do_click((By.ID, self.cut_grade_standard), allure_Screenshot_name)

    def Click_Table_ref_num(self, allure_controlKeydown_screenshot_name,allure_mouse_hover_screenshot_name):
        self.get_mouse_hover((By.CSS_SELECTOR,self.Table_ref_num),  allure_mouse_hover_screenshot_name)
        self.get_control_Keydown_actions(self,'c')
    def Click_Create_new_memo(self, allure_Screenshot_name):
        self.do_click((By.ID, self.Create_memo),allure_Screenshot_name)
    def Click_vendor(self,Text, allure_Screenshot_name):
        self.do_click((By.ID, self.Click_Vendor),allure_Screenshot_name)
        self.do_enter_text((By.CSS_SELECTOR, self.Enter_Vendor),Text, allure_Screenshot_name)
        self.do_press_enter((By.CSS_SELECTOR, self.Enter_Vendor), allure_Screenshot_name)
    def Click_Submit_Button(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.Click_Submit),allure_Screenshot_name)
    def Click_Add_Stone(self, allure_Screenshot_name):
        self.do_click((By.ID, self.Add_Stone),allure_Screenshot_name)
    def Click_Stone_type(self,Text, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.Stone_type),allure_Screenshot_name)
        self.do_enter_text((By.CSS_SELECTOR, self.Enter_Stones),Text, allure_Screenshot_name)
        self.do_press_enter((By.CSS_SELECTOR, self.Enter_Stones), allure_Screenshot_name)

    def Enter_no_of_stones(self, Numeric_Value, allure_Screenshot_name):
        self.do_enter_text((By.CSS_SELECTOR, self.no_of_stones), Numeric_Value, allure_Screenshot_name)
    def Enter_submit_button(self, allure_Screenshot_name):
        self.do_click((By.ID, self.submit_button),allure_Screenshot_name)







