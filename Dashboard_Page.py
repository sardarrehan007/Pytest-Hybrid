from selenium.webdriver.common.by import By

from DataDriven import TestData
from Librariries import *
from Main.CorePage import CorePage
from selenium.webdriver.common.keys import Keys

def send_keys(param):
    pass


class DashboardPage(CorePage):

    #Invoice_received=TestData.json_dashboard_r["Dashboard"]["Invoice_received"]



    def __init__(self, driver):
        super().__init__(driver)

    # def Create_Quotation_btn(self,  allure_Screenshot_name):
    #   self.do_click((By.ID, TestData.json_dashboard_id_["Dashboard"]["btn_create_quotation_Id"]),  allure_Screenshot_name)
    def Click_Catalog(self, allure_Screenshot_name):
         self.do_click((By.ID, self.gem_stone_catalog),allure_Screenshot_name)

    def Click_My_Inventory(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.my_inventory), allure_Screenshot_name)

    #def Click_Checkbox_stone(self, allure_Screenshot_name):
     #   self.do_click((By.XPATH, self.check_box_stone), allure_Screenshot_name)

    #def Click_print_label(self, allure_Screenshot_name):
      #  self.do_click((By.XPATH, self.print_label), allure_Screenshot_name)

    #def enter_data(self, numeric_value , allure_Screenshot_name):
     #   self.do_enter_text((By.XPATH, self.print_sticker), numeric_value , allure_Screenshot_name)
      #  self.do_press_enter((By.XPATH, self.print_sticker),allure_Screenshot_name)


    def Click_Memo(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.Record_a_memo), allure_Screenshot_name)
    def Click_dropdown(self, allure_Screenshot_name):
        self.do_dropdown_by_index((By.ID, "#supplier_dropdown"), '5',allure_Screenshot_name)

    def Click_dropdown_value(self, allure_Screenshot_name):
        self.do_dropdown_by_value((By.XPATH, "//*[@id='supplier_dropdown']/option[3]"), "3", allure_Screenshot_name)
    def Click_add_button(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.add_stones_supplier), allure_Screenshot_name)
    def enter_num(self, numeric_value , allure_Screenshot_name):
       self.do_enter_text((By.XPATH, self.num_of_stones), numeric_value , allure_Screenshot_name)
       self.do_press_enter((By.XPATH, self.num_of_stones),allure_Screenshot_name)
    def add_stones(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.click_dropdown_to_add_stones), allure_Screenshot_name)
    def enter_name(self, Text , allure_Screenshot_name):
       self.do_enter_text((By.CSS_SELECTOR, self.enter_name_stone), Text , allure_Screenshot_name)
       self.do_press_enter((By.CSS_SELECTOR, self.enter_name_stone),allure_Screenshot_name)
    def memo_received(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.memo_received1), allure_Screenshot_name)
   # def memo_received(self, allure_Screenshot_name):
      #  self.do_click((By.XPATH, self.memo_received1), allure_Screenshot_name)
    def ok_click1(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.click_ok), allure_Screenshot_name)
    def back_click1(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.back_click), allure_Screenshot_name)

    def check_stones(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.checkbox_stone), allure_Screenshot_name)
    def click_convert_to_invoice(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.convert_to_invoice), allure_Screenshot_name)

    def alert_memo_conversion1(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.alert_memo_conversion), allure_Screenshot_name)
    def Accounting_dropdown1(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.Accounting_dropdown), allure_Screenshot_name)
    def Supplier_Invoices1(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.Supplier_invoices), allure_Screenshot_name)
    def Open_invoice1(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.open_invoice), allure_Screenshot_name)
    def Currency_Selector(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.currency_seletor), allure_Screenshot_name)
    def search_currency1(self, text , allure_Screenshot_name):
       self.do_enter_text((By.CSS_SELECTOR, self.search_currency), text , allure_Screenshot_name)
       self.do_press_enter((By.CSS_SELECTOR, self.search_currency),allure_Screenshot_name)
    def Weight_assign1(self, Numeric_value , allure_Screenshot_name):
       self.do_double_click((By.XPATH, self.Weight_assign), allure_Screenshot_name)
       self.do_enter_text((By.XPATH, self.Weight_enter), Numeric_value , allure_Screenshot_name)
       self.do_press_enter((By.XPATH, self.Weight_enter),allure_Screenshot_name)
    def Cost_1(self, Numeric_value , allure_Screenshot_name):
       self.do_double_click((By.XPATH, self.Cost), allure_Screenshot_name)
       self.do_enter_text((By.XPATH, self.Cost_Enter), Numeric_value , allure_Screenshot_name)
       self.do_press_enter((By.XPATH, self.Cost_Enter),allure_Screenshot_name)
    def Total_Cost1(self, Numeric_value , allure_Screenshot_name):
       self.do_double_click((By.XPATH, self.Total_cost), allure_Screenshot_name)
       self.do_enter_text((By.XPATH, self.Total_Cost_Enter), Numeric_value , allure_Screenshot_name)
       self.do_press_enter((By.XPATH, self.Total_Cost_Enter),allure_Screenshot_name)

    def Record(self, allure_Screenshot_name):
       self.do_click((By.XPATH, self.Record_payment), allure_Screenshot_name)
    def payment_method1(self, allure_Screenshot_name):
        self.do_click((By.XPATH, self.payment_method), allure_Screenshot_name)

    def Click_dropdown_value234(self, allure_Screenshot_name):
        self.do_dropdown_by_value((By.XPATH, "/html/body/div[2]/div/div/form/div[1]/div/div/div/div/div[1]/div/div[1]/select/option[3]"), "2", allure_Screenshot_name)
    def client_sent1(self,numeric_value, allure_Screenshot_name):
        self.do_enter_text((By.XPATH, self.search_currency), numeric_value, allure_Screenshot_name)
        self.do_press_enter((By.XPATH, self.search_currency), allure_Screenshot_name)
    def Click_Invoice_received(self, allure_Screenshot_name):
        self.do_click((By.CSS_SELECTOR, self.Invoice_received), allure_Screenshot_name)

