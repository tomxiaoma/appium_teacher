from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class BaseView(object):

    def __init__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        try:
            return WebDriverWait(self.driver, 10, 1).until(EC.visibility_of_element_located(*loc))
        except Exception as msg:
            logging.error("未找到元素")
            raise msg

    def find_elements(self,*loc):
        try:
            return WebDriverWait(self.driver, 10, 1).until(EC.visibility_of_element_located(*loc))
        except Exception as msg:
            logging.error("未找到元素")
            raise msg

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self,start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)


