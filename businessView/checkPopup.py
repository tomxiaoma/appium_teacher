import logging
from common.common_fun import Common
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class CheckPopup(Common):

    #手机号
    phone = (By.ID, 'com.yiqizhangda.teacher:id/et_number')

    #首页发布按钮
    publish_button = (By.XPATH, '//*[@class="android.widget.RelativeLayout" and @index="2"]')

    #弹框
    win_frame = (By.ID, 'com.yiqizhangda.teacher:id/recommend_close')

    def check_slide(self):
        """
        检测教师端是否有闪屏，有的话就滑动，没有就直接进入下一步
        :return:
        """
        try:
            self.driver.find_element(*self.phone) or self.driver.find_element(*self.publish_button)
        except NoSuchElementException as msg:
            logging.info("开始滑动闪屏.....")
            for i in range(4):
                self.swipeLeft()
            sleep(2)
            TouchAction(self.driver).tap(x=443, y=1193).perform()
        else:
            pass

    def check_window(self):
        """
        检测是否有弹窗，如果有弹窗，关闭掉
        :return:
        """
        try:
            self.driver.find_element(*self.win_frame)
        except NoSuchElementException as msg:
            pass
        else:
            self.driver.find_element(*self.win_frame).click()