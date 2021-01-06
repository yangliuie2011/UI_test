#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Chris

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from util.openDriver import OpenDriver
from util.logger import Logger
import time
import os.path
logger = Logger(logger="WebDriver").getlog()


class WebDriver(object):
    '''
        Base framework for the main class, the original
    selenium provided by the method of the two packaging,
    making it easier to use.
    '''
    def __init__(self):
        web_driver = OpenDriver()
        self.driver = web_driver.driver()
        logger.info("Init a WebDriver.")

    def element_wait(self, ele_type, value, secs=5):
        '''
        Waiting for an element to display.
        '''
        logger.info("wait for %d seconds." % secs)
        if ele_type == "id":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)))
        elif ele_type == "name":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)))
        elif ele_type == "class":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif ele_type == "link_text":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif ele_type == "xpath":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif ele_type == "css":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            logger.error("NoSuchElementTypeException: %s" % ele_type)
            self.get_screenshot()
            raise NoSuchElementException(
                "Not find element, Please check the syntax error.")


    #查找元素的方法
    def get_element(self, css):
        '''
        Judge element positioning way, and returns the element.
        '''
        element = ''
        if "=>" not in css:
            ele_type = "css"
            value = ele_type
            # wait element.
            self.element_wait(ele_type, css)
        else:
            #用=>进行剥离
            ele_type = css.split("=>")[0] #id
            value = css.split("=>")[1] #su
            if ele_type == "" or value == "":
                raise NameError(
                    "Grammatical errors,reference: 'id=>useranme'.")
            self.element_wait(ele_type, value)

        if ele_type == "id":
            try:
                element = self.driver.find_element_by_id(value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, ele_type, value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif ele_type == "name":
            try:
                element = self.driver.find_element_by_name(value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, ele_type, value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif ele_type == "class":
            try:
                element = self.driver.find_element_by_class_name(value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, ele_type, value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif ele_type == "link_text":
            try:
                element = self.driver.find_element_by_link_text(value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, ele_type, value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif ele_type == "xpath":
            try:
                element = self.driver.find_element_by_xpath(value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, ele_type, value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        elif ele_type == "css":
            try:
                element = self.driver.find_element_by_css_selector(value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, ele_type, value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
        else:
            logger.error("NoSuchElementTypeException: %s" % ele_type)
            self.get_screenshot()
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def open(self, url):
        '''
        open url.

        Usage:
        driver.open("https://www.baidu.com")
        '''
        self.driver.get(url)
        logger.info("Open url: %s" % url)

    def max_window(self):
        '''
        Set browser window maximized.

        Usage:
        driver.max_window()
        '''
        self.driver.maximize_window()
        logger.info("Set browser window maximized")

    def set_window(self, wide, high):
        '''
        Set browser window wide and high.

        Usage:
        driver.set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)
        logger.info(" Set browser window %s wide and  %s high." % (wide, high))

    def type(self, css, text):
        '''
        Operation input box.

        Usage:
        driver.type("css=>#el","selenium")
        '''
        el = self.get_element(css)
        el.send_keys(text)
        logger.info(" Input text %s to %s element." % (text, css))

    def clear(self, css):
        '''
        Clear the contents of the input box.

        Usage:
        driver.clear("css=>#el")
        '''
        el = self.get_element(css)
        el.clear()
        logger.info("  Clear the contents of the input box %s." % css)

    def clear_cookie(self):
        '''
        Clear the contents of the input box.

        Usage:
        driver.clear("css=>#el")
        '''
        el = self.driver.delete_all_cookies()
        logger.info("  Clear the cookies .")

    def add_cookie(self, name, value):
        '''
        Clear the contents of the input box.

        Usage:
        driver.clear("css=>#el")
        '''
        el = self.driver.add_cookie({"name": name, "value": value})
        logger.info("  Add cookie in to brower." )

    def click(self, css):
        '''
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("css=>#el")
        '''
        el = self.get_element(css)
        el.click()
        logger.info("Click the element %s." % css)

    def right_click(self, css):
        '''
        Right click element.

        Usage:
        driver.right_click("css=>#el")
        '''
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()
        logger.info("Right click the element %s." % css)

    def move_to_element(self, css):
        '''
        Mouse over the element.

        Usage:
        driver.move_to_element("css=>#el")
        '''
        el = self.get_element(css)
        ActionChains(self.driver).move_to_element(el).perform()
        logger.info("Move to the element %s." % css)

    def double_click(self, css):
        '''
        Double click element.

        Usage:
        driver.double_click("css=>#el")
        '''
        el = self.get_element(css)
        ActionChains(self.driver).double_click(el).perform()
        logger.info("Double click element %s." % css)

    def drag_and_drop(self, el_css, ta_css):
        '''
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("css=>#el","css=>#ta")
        '''
        element = self.get_element(el_css)
        target = self.get_element(ta_css)
        ActionChains(self.driver).drag_and_drop(element, target).perform()
        logger.info("drag_and_drop from %s to %s." % (el_css, ta_css))

    def click_text(self, text):
        '''
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        '''
        self.driver.find_element_by_partial_link_text(text).click()
        logger.info("Click the element by the link text." % text)

    def close(self):
        '''
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        '''
        self.driver.close()
        logger.info("Close the driver." )

    def quit(self):
        '''
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        '''
        self.driver.quit()
        logger.info("Quit the driver and close all the windows.")

    def submit(self, css):
        '''
        Submit the specified form.

        Usage:
        driver.submit("css=>#el")
        '''
        el = self.get_element(css)
        el.submit()
        logger.info("Submit the specified form %s." % css)

    def F5(self):
        '''
        Refresh the current page.

        Usage:
        driver.F5()
        '''
        self.driver.refresh()
        logger.info("Refresh the current page.")

    def js(self, script):
        '''
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)
        logger.info("Execute JavaScript scripts. %s" % script)

    def get_attribute(self, css, attribute):
        '''
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("css=>#el","type")
        '''
        el = self.get_element(css)
        logger.info("Gets the value %s of an element attribute %s" % (attribute, css))
        return el.get_attribute(attribute)

    def get_text(self, css):
        '''
        Get element text information.

        Usage:
        driver.get_text("css=>#el")
        '''
        el = self.get_element(css)
        logger.info("Get element text information.. %s" % css)
        return el.text

    def get_display(self, css):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("css=>#el")
        '''
        el = self.get_element(css)
        logger.info("The %s element is exits or not" % css)
        return el.is_displayed()

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        logger.info("Get window title.")
        return self.driver.title

    def get_page_source(self):
        '''
        Get page source.

        Usage:
        driver.get_title()
        '''
        logger.info("Get page source.")
        return self.driver.page_source

    def get_url(self):
        '''
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        '''
        logger.info("Get the URL address of the current page.")
        return self.driver.current_url

    def get_alert_text(self):
        '''
        Gets the text of the Alert.

        Usage:
        driver.get_alert_text()
        '''
        logger.info("Gets the text of the Alert.")
        return self.driver.switch_to.alert.text

    def wait(self, secs):
        '''
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)
        logger.info("wait for %d seconds." % secs)

    def accept_alert(self):
        '''
        Accept warning box.

        Usage:
        driver.accept_alert()
        '''
        self.driver.switch_to.alert.accept()
        logger.info("Accept warning box.")

    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()
        logger.info("Dismisses the alert available.")

    def switch_to_frame(self, css):
        '''
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("css=>#el")
        '''
        iframe_el = self.get_element(css)
        self.driver.switch_to.frame(iframe_el)
        logger.info("Switch to %s frame." % css)

    def switch_to_frame_out(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver.switch_to.default_content()
        logger.info("Switch to the default frame.")

    def open_new_window(self, css):
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window("link_text=>注册")
        '''
        original_window = self.driver.current_window_handle
        el = self.get_element(css)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                logger.info("Open the new window and switch the handle to the newly opened window.")

    def get_screenshot(self):
        '''Saves a screenshot of the current window to a PNG image file.

        Usage:
        driver.get_screenshot('/Screenshots/foo.png')
        '''
        # self.driver.get_screenshot_as_file(file_path)
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots + %s" % rq)
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_screenshot()

    def get_screenshot_file(self, name):
        '''Saves a screenshot of the current window to a PNG image file.

        Usage:
        driver.get_screenshot('/Screenshots/foo.png')
        '''
        # self.driver.get_screenshot_as_file(file_path)
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + name + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Test case is failed, keep a screenshot: /screenshots + %s" % rq)
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_screenshot()

    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

    def select(self, css, value):
        '''
        Constructor. A check is made that the given element is, indeed, a SELECT tag. If it is not,
        then an UnexpectedTagNameException is thrown.

        :Args:
         - css - element SELECT element to wrap
         - value - The value to match against

        Usage:
            <select name="NR" id="nr">
                <option value="10" selected="">每页显示10条</option>
                <option value="20">每页显示20条</option>
                <option value="50">每页显示50条</option>
            </select>

            driver.select("#nr", '20')
            driver.select("xpath=>//[@name='NR']", '20')
        '''
        el = self.get_element(css)
        Select(el).select_by_value(value)


if __name__ == '__main__':
    WD = WebDriver()

    WD.open("http://www.baidu.com")
    print(WD.get_page_source())
    WD.get_screenshot()
    WD.quit()
