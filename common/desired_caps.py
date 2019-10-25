from appium import webdriver
from config.loggingReader import *
from config.yamlReader import *


def appium_desired() :
    """
    封装APP启动的参数，直接从yaml中读取数据
    """
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']

    logging.info('启动app...')
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    appium_desired()



