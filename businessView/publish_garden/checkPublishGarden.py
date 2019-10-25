import logging
from common.common_fun import Common
from selenium.common.exceptions import NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from time import sleep
from businessView.checkPopup import CheckPopup


class CheckGarden(Common):
    home_garden = (By.ID,'com.yiqizhangda.teacher:id/home_garden_activity_icon')

    def check_publish_success(self,title):
        """
        校验发布是否成功
        :param title:
        :return:
        """
        logging.info("检测在园时光是否发送成功")
        try :
            sleep(3)
            self.driver.find_element(*self.home_garden).click()
            self.driver.find_element(By.XPATH,"//*[@resource-id ='com.yiqizhangda.teacher:id/feed_title'] " and
                                     "//android.widget.TextView[contains(@text," + "'" + title + "'" + ")]")
        except NoSuchElementException:
            logging.error('发布失败!')
            self.getScreenShot('发布失败')
            return False
        else:
            logging.info('发布成功!')
            return True

    def check_success(self, num):
        """
        校验指定发送是否成功
        :param num:
        :return:
        """
        logging.info("检测在园时光指定发送是否发送成功")
        try:
            sleep(3)
            self.driver.find_element(*self.home_garden).click()
            self.driver.find_element(By.XPATH, "//*[@resource-id ='com.yiqizhangda.teacher:id/feed_collect_info'] " and
                                     "//android.widget.TextView[contains(@text," + "'" + num + "已放入成长册'" + ")]")
        except NoSuchElementException:
            logging.error('发布失败!')
            self.getScreenShot('发布失败')
            return False
        else:
            logging.info('发布成功!')
            return True

