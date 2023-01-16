from datetime import datetime

from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from Librariries import *


class CorePage:
    def __init__(self, driver):
        self.driver = driver

    '''Use in PageObject '''

    def do_enter_text(self, by_Locator_type, usertext_data, allure_entertext_screenshot_name):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type)).clear()
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type)).send_keys(
                usertext_data)
            self.get_allure_screenshot("Enter Text [ Perform ]:- " + allure_entertext_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot("Enter Text [ Not Perform ]:- " + allure_entertext_screenshot_name + str(e))
            return False

    def do_clear_text(self, by_Locator_type, allure_cleartext_screenshot_name):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type)).clear()
            self.get_allure_screenshot("Clear Text [ Perform ]:- " + allure_cleartext_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot("Clear Text [ Not Perform ]:- " + allure_cleartext_screenshot_name + str(e))
            return False

    def do_click(self, by_Locator_type_and_value, allure_click_element_screenshot_name) -> object:
        """

        :rtype: object
        """
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type_and_value)).click()
            self.get_allure_screenshot("Click [ Perform ]:- " + allure_click_element_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot("Click [ Not Perform ]:- " + allure_click_element_screenshot_name + str(e))
            return False

    def do_press_enter(self, by_Locator_type_and_value, allure_press_enter_screenshot_name):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type_and_value)).send_keys(
                Keys.ENTER)
            self.get_allure_screenshot("Enter [ Perform ]:- " + allure_press_enter_screenshot_name)
            return True
        except Exception as e:
            self.get_allure_screenshot("Enter [ Not Perform ]:- " + allure_press_enter_screenshot_name + str(e))
            return False

    def do_press_keys(self, by_Locator_type_and_value, keys, allure_press_keys_screenshot_name):
        try:
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type_and_value)).send_keys(
                keys)
            self.get_allure_screenshot("Enter [ Perform ]:- " + allure_press_keys_screenshot_name)
            return True
        except Exception as e:
            self.get_allure_screenshot("Enter [ Not Perform ]:- " + allure_press_keys_screenshot_name + str(e))
            return False

    def do_double_click(self, by_Locator_type_and_value, allure_double_click_element_screenshot_name):
        try:
            dbclick = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type_and_value))
            actionChains = ActionChains(self.driver)
            actionChains.double_click(dbclick).perform()
            self.get_allure_screenshot("Double Click [ Perform ]:- " + allure_double_click_element_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot(
                "Double Click [ Not Perform ]:- " + allure_double_click_element_screenshot_name + str(e))
            return False

    def do_dropdown_by_value(self, by_Locator_type_and_value, dropdown_text, allure_dropdown_screenshot_name):
        try:
            drop_drown = Select(
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type_and_value)))
            drop_drown.select_by_value(dropdown_text)
            self.get_allure_screenshot("Drop Down [ Perform ]:- " + allure_dropdown_screenshot_name)
            return True
        except Exception as e:
            self.get_allure_screenshot("Drop Down [ Not Perform ]:- " + allure_dropdown_screenshot_name + str(e))
            return False

    def do_dropdown_by_index(self, by_Locator_type_and_value, dropdown_index, allure_dropdown_screenshot_name):
        try:
            drop_drown = Select(
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type_and_value)))
            drop_drown.select_by_index(dropdown_index)
            self.get_allure_screenshot("Drop Down [ Perform ]:- " + allure_dropdown_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot("Drop Down [ Not Perform ]:- " + allure_dropdown_screenshot_name + str(e))
            return False

    def do_dropdown_by_visible_text(self, by_Locator_type_and_value, dropdown_visible_text,
                                    allure_dropdown_screenshot_name):
        try:
            drop_drown = Select(
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type_and_value)))
            drop_drown.select_by_visible_text(dropdown_visible_text)
            self.get_allure_screenshot("Drop Down [ Perform ]:- " + allure_dropdown_screenshot_name)
            return True
        except Exception as e:
            self.get_allure_screenshot("Drop Down [ Not Perform ]:- " + allure_dropdown_screenshot_name + str(e))
            return False

    def do_dropdown_by_click_input_enter(self, by_ClickLocator_type_and_value, by_InputLocator_type_and_value,
                                         input_text, allure_dropdown_screenshot_name):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(by_ClickLocator_type_and_value)).click()
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(by_InputLocator_type_and_value)).send_keys(input_text)
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(by_InputLocator_type_and_value)).send_keys(Keys.ENTER)

            self.get_allure_screenshot("Drop Down [ Perform ]:- " + allure_dropdown_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot("Drop Down [ Not Perform ]:- " + allure_dropdown_screenshot_name + str(e))
            return False

    '''Use in making test cases'''

    def is_wait_sleep(self, duration):
        try:
            time.sleep(duration)
            return True
        except Exception as e:
            self.get_allure_screenshot("Wait Sleep [ Not Perform ]:- " + str(e))
            return False

    def is_wait_implicit(self, time_imp_duration, allure_wait_implicit_screenshot_name):
        try:
            self.driver.implicitly_wait(time_imp_duration)
            self.get_allure_screenshot("Wait Implicit [ Perform ]:- " + allure_wait_implicit_screenshot_name)
            return True
        except Exception as e:
            self.get_allure_screenshot(
                "Wait Implicit [ Not Perform ]:- " + allure_wait_implicit_screenshot_name + str(e))
            return False

    def is_wait_page_load(self, page_time, allure_pageload_screenshot_name):
        try:
            self.driver.set_page_load_timeout(page_time)
            self.get_allure_screenshot("Wait Page Load [ Perform ]:- " + allure_pageload_screenshot_name)
            return True
        except Exception as e:
            self.get_allure_screenshot("Wait Page Load [ Not Perform ]:- " + allure_pageload_screenshot_name + str(e))
            return False

    def is_fullScreen_window(self, allure_fullscreen_screenshot_name):
        try:
            self.driver.fullscreen_window()
            self.get_allure_screenshot("FullScreen [ Perform ]:- " + allure_fullscreen_screenshot_name)
            return True
        except Exception as e:
            self.get_allure_screenshot("FullScreen [ Not Perform ]:- " + allure_fullscreen_screenshot_name + str(e))
            return False

    def is_scroll_in_position(self, x, y, allure_scroll_screenshot_name):
        try:
            self.driver.execute_script("window.scrollTo(" + x + " , " + y + ")")
            self.get_allure_screenshot("Scroll To Position [ Perform ]:- " + allure_scroll_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot("Scroll To Position [ Not Perform ]:- " + allure_scroll_screenshot_name + str(e))
            return False

    def is_title(self, expected_title, allure_Title_screenshot_name):
        try:
            if self.driver.title == expected_title:
                self.get_allure_screenshot("Title Get [ If Perform ]:- " + allure_Title_screenshot_name)
                assert True
            else:
                self.get_allure_screenshot("Title Not Get [  Else Perform ]:- " + allure_Title_screenshot_name)
                self.driver.close()

        except NoSuchElementException as e:
            self.get_allure_step_screenshot("Title Get [ Not Perform ]:- ", allure_Title_screenshot_name + str(e))
            return False

    def is_switch_to_default_content(self, allure_switchdefaultContent_screenshot_name):
        try:
            self.driver.switch_to.default_content()
            self.get_allure_screenshot(
                "Switch BY Default Content [ Perform ]:- " + allure_switchdefaultContent_screenshot_name)
            return True
        except Exception as e:
            self.get_allure_screenshot(
                "Switch BY Default Content [ Not Perform ]:- " + allure_switchdefaultContent_screenshot_name + str(e))
            return False

    def is_new_tab(self, allure_new_tab_screenshot_name):
        try:
            time.sleep(2)
            self.driver.execute_script("window.open('');")
            time.sleep(2)
            self.get_allure_screenshot("New Window [ Perform ]:- " + allure_new_tab_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot("New Window [ Not Perform ]:- " + allure_new_tab_screenshot_name + str(e))
            return False

    def is_tab_switch(self, window_index, allure_is_tab_switch_screenshot_name):
        try:
            self.driver.switch_to.window(self.driver.window_handles[window_index])
            self.get_allure_screenshot("Window index [ Perform ]:- " + allure_is_tab_switch_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot(
                "Window index [ Not Perform ]:- " + allure_is_tab_switch_screenshot_name + str(e))
            return False

    def is_delete_cookies(self, allure_cookies_screenshot_name):
        try:
            self.driver.delete_all_cookies()
            self.get_allure_screenshot("Switch BY Default Content [ Perform ]:- " + allure_cookies_screenshot_name)
            return True
        except Exception as e:
            self.get_allure_screenshot(
                "Switch BY Default Content [ Not Perform ]:- " + allure_cookies_screenshot_name + str(e))
            return False

    def is_getting_cookies(self, allure_cookies_screenshot_name):
        try:
            self.driver.getCookies()
            self.get_allure_screenshot("Switch BY Default Content [ Perform ]:- " + allure_cookies_screenshot_name)
            return True
        except Exception as e:
            self.get_allure_screenshot(
                "Switch BY Default Content [ Not Perform ]:- " + allure_cookies_screenshot_name + str(e))
            return False

    '''Use in PageObject and test cases too if you handle ids in test cases'''

    def get_url(self, url, allure_Url_screenshot_name):
        try:
            self.driver.get(url)
            self.get_allure_screenshot("Get Url [ Perform ]:- " + allure_Url_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot("Get Url [ Not Perform ]:- " + allure_Url_screenshot_name + str(e))
            return False

    def get_mouse_hover(self, by_Locator_type, allure_mouse_hover_screenshot_name):
        try:
            element_to_hover_over = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(by_Locator_type))
            hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
            hover.perform()
            self.get_allure_screenshot("Scroll To Element [ Perform ]:- " + allure_mouse_hover_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot(
                "Scroll To Element [ Not Perform ]:- " + allure_mouse_hover_screenshot_name + str(e))
            return False

    def get_click_and_hold(self, by_Locator_type, allure_click_and_hold_screenshot_name):
        try:
            element_to_hover_over = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(by_Locator_type))
            hover = ActionChains(self.driver).click_and_hold(element_to_hover_over)
            hover.perform()
            self.get_allure_screenshot("Scroll To Element [ Perform ]:- " + allure_click_and_hold_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot(
                "Scroll To Element [ Not Perform ]:- " + allure_click_and_hold_screenshot_name + str(e))
            return False

    def get_scroll_in_element(self, by_Locator_type, allure_scroll_screenshot_name):
        try:
            elements = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type))
            self.driver.execute_script("arguments[0].scrollIntoView();", elements)
            self.get_allure_screenshot("Scroll To Element [ Perform ]:- " + allure_scroll_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot("Scroll To Element [ Not Perform ]:- " + allure_scroll_screenshot_name + str(e))
            return False

    def get_switch_to_iframe_by_index_number(self, by_Locator, indexNumber, allure_iframe_screenshot_name):
        try:
            iframe = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator))[indexNumber]
            self.driver.switch_to.frame(iframe)
            self.get_allure_screenshot("Iframe By Index [ Perform ]:- " + allure_iframe_screenshot_name)
            return True
        except Exception as e:
            self.get_allure_screenshot("Iframe By Index [ Not Perform ]:- " + allure_iframe_screenshot_name + str(e))
            return False

    def get_switch_to_iframe_by_tag_name(self, by_tagName, allure_iframe_screenshot_name):
        try:
            iframe = self.driver.find_elements_by_tag_name(by_tagName)
            self.driver.switch_to.frame(iframe)
            self.get_allure_screenshot("Iframe By TageName [ Perform ]:- " + allure_iframe_screenshot_name)
            return True
        except Exception as e:
            self.get_allure_screenshot("Iframe By TageName [ Not Perform ]:- " + allure_iframe_screenshot_name + str(e))
            return False

    def get_input_current_date(self, by_Locator_type_and_value, allure_currentdate_screenshot_name,
                               date=datetime.now()):
        try:
            elem = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type_and_value))
            elem.send_keys(datetime.strftime(date, "%m/%d/%Y"))
            self.get_allure_screenshot("Current Date [ Perform ]:- " + allure_currentdate_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot("Current Date [ Not Perform ]:- " + allure_currentdate_screenshot_name + str(e))
            return False

    def get_input_date_time(self, by_Locator_type_and_value, allure_datetime_screenshot_name, date_time=datetime.now()):
        try:
            elem = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type_and_value))
            elem.send_keys(datetime.strftime(date_time, "%m/%d/%Y %H:%M:%S"))
            datetime.now(), "%m/%d/%Y %H:%M:%S"
            self.get_allure_screenshot("Date Time [ Perform ]:- " + allure_datetime_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot("Date Time [ Not Perform ]:- " + allure_datetime_screenshot_name + str(e))
            return False

    def get_element_text(self, by_Locator_type_and_value, allure_getelementtext_screenshot_name):
        try:
            actual_text = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(by_Locator_type_and_value))
            self.get_allure_screenshot("Get Element Text [ Perform ]:- " + allure_getelementtext_screenshot_name)
            return actual_text.text, True
        except NoSuchElementException as e:
            self.get_allure_screenshot(
                "Get Element Text [ Not Perform ]:- " + allure_getelementtext_screenshot_name + str(e))
            return False

    def get_element_visible(self, by_Locator_type_and_value, allure_elementvisible_screenshot_name):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_Locator_type_and_value))
            self.get_allure_screenshot("Element Visible [ Perform ]:- " + allure_elementvisible_screenshot_name)
            return bool(element)
        except NoSuchElementException as e:
            self.get_allure_screenshot(
                "Element Visible [ Not Perform ]:- " + allure_elementvisible_screenshot_name + str(e))
            return False

    def get_control_Keydown_actions(self, control_actions_in_string, allure_controlKeydown_screenshot_name):
        """

        :rtype: object
        """
        try:
            actions = ActionChains(self.driver)
            actions.key_down(Keys.CONTROL).send_keys(control_actions_in_string).perform()
            self.get_allure_screenshot(
                "Control Actions [ Perform ]:- " + control_actions_in_string + " - " + allure_controlKeydown_screenshot_name)
            # self.get_control_action_keyup(allure_controlKeydown_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot(
                "Control Actions [ Not Perform ]:- " + control_actions_in_string + " - " + allure_controlKeydown_screenshot_name + str(
                    e))
            return False

    def get_control_action_keyup(self, allure_keyup_screenshot_name):
        try:
            actions = ActionChains(self.driver)
            actions.key_up(Keys.CONTROL).perform()
            self.get_allure_screenshot("Control Actions KeyUp [ Perform ]:- " + allure_keyup_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot(
                "Control Actions KeyUp [ Not Perform ]:- " + allure_keyup_screenshot_name + str(e))

            return False

    def get_upload_image_with_path(self, path, allure_upload_screenshot_name):
        try:
            Image.open(path)
            self.get_allure_screenshot("Image Upload [ Perform ]:- " + allure_upload_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot("Image Upload [ Not Perform ]:- " + allure_upload_screenshot_name + str(e))
            return False

    def get_upload_file_with_path(self, path, allure_upload_screenshot_name):
        try:
            self.is_wait_sleep(2)
            self.driver.find_element_by_xpath("//*[@id='addDocumentForm2']/div/div/div[1]/input").send_keys(path)
            self.is_wait_sleep(2)
            self.get_allure_screenshot("File Upload [ Perform ]:- " + allure_upload_screenshot_name)
            return True
        except NoSuchElementException as e:
            self.get_allure_screenshot("File Upload [ Not Perform ]:- " + allure_upload_screenshot_name + str(e))
            return False

    '''Allure Methods '''

    def get_simple_screenshot(self, ScreenshotName, ):
        try:
            self.driver.get_screenshot_as_file(
                "ScreenShots/" + ('%s ' % time.strftime("%Y-%m-%d--%H-%M-%S_") + ScreenshotName + "_.png"))
        except Exception as e:
            print(str(e))

    def get_allure_step_screenshot(self, allure_Step, allure_description_name):
        try:
            with allure.step(allure_Step):
                allure.attach(self.driver.get_screenshot_as_png(), name=allure_description_name,
                              attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(str(e))

    def get_allure_screenshot(self, allure_screenshot_name):
        try:
            allure.attach(self.driver.get_screenshot_as_png(), name=allure_screenshot_name,
                          attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(str(e))
