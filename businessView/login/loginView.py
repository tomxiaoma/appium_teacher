import logging
from common.common_fun import Common
from selenium.common.exceptions import NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from businessView.checkPopup import CheckPopup


class LoginView(Common):
    # 登录-输入手机号码定位
    phone = (By.ID, 'com.yiqizhangda.teacher:id/et_number')
    phone_button = (By.ID, 'com.yiqizhangda.teacher:id/bt_next_num')

    # 登录-输入密码定位
    password = (By.ID, 'com.yiqizhangda.teacher:id/et_password')
    loginBtn = (By.ID, 'com.yiqizhangda.teacher:id/bt_login')

    #检测登录
    check_myinfo = (By.ID,'com.yiqizhangda.teacher:id/home_range')

    # 退出登录
    my_info = (By.XPATH, '//android.widget.TextView[contains(@text,"我的")]')
    set_up = (By.ID, 'com.yiqizhangda.teacher:id/mine_setting_layout')
    sign_out = (By.ID, 'com.yiqizhangda.teacher:id/setting_action_logout')
    alert_confirm = (By.XPATH, '//android.widget.Button[@text="确定"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.Common = Common(driver)
        self.checkPopup = CheckPopup(driver)

    def login_action(self,username,password):
        """
        教师端登录
        :param mawentao:
        :param password:
        :return:
        """
        logging.info('============登录开始==============')
        logging.info('输入手机号码:%s' %username)
        self.driver.find_element(*self.phone).send_keys(username)
        logging.info("点击下一步")
        self.driver.find_element(*self.phone_button).click()

        logging.info('输入密码:%s'%password)
        self.driver.find_element(*self.password).send_keys(password)
        logging.info('点击下一步登录')
        self.driver.find_element(*self.loginBtn).click()

    def check_loginStatus(self):
        logging.info('====检测登录======')
        try:
            self.driver.find_element(*self.check_myinfo)
        except NoSuchElementException:
            logging.error('登录失败!')
            self.getScreenShot('登录失败')
            return False
        else:
            logging.info('登录成功!')
            #self.logout_action()
            return True

    def logout_action(self):
        logging.info('=====退出登录======')
        self.driver.find_element(*self.my_info).click()
        self.driver.find_element(*self.set_up).click()
        self.driver.find_element(*self.sign_out).click()
        self.driver.find_element(*self.alert_confirm).click()


if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    l.checkPopup.check_slide()
    l.login_action('15900796431','123123')
    l.check_loginStatus()
    #l.logout_action()
