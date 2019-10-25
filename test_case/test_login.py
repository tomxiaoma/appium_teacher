from common.myunit import StartEnd
from businessView.login.loginView import LoginView
import unittest
import logging


class TestLogin(StartEnd):
    csv_file='../data/account.csv'

    def test_teacher_login(self):
        logging.info('==================正确的账号登录=================')
        l=LoginView(self.driver)
        l.checkPopup.check_slide()
        data=l.get_csv_data(self.csv_file,1)

        l.login_action(data[0],data[1])
        self.assertTrue(l.check_loginStatus())


    def test_login_yqzd_pwd(self):
        logging.info('==================错误的账号登录==================')
        l=LoginView(self.driver)
        l.checkPopup.check_slide()
        data=l.get_csv_data(self.csv_file,2)

        l.login_action(data[0],data[1])
        self.assertTrue(l.check_loginStatus())



if __name__ == '__main__':
    unittest.main()