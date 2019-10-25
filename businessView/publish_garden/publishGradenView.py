import logging
from common.common_fun import Common
from selenium.common.exceptions import NoSuchElementException
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from time import sleep
from businessView.checkPopup import CheckPopup
from businessView.publish_garden.checkPublishGarden import CheckGarden


class PublishPic(Common):

    #首页发布按钮
    publish_button = (By.XPATH,'//*[@class="android.widget.RelativeLayout" and @index="2"]')

    #选择发布方式
    publish_garden = (By.ID,'com.yiqizhangda.teacher:id/action_publish_feed')

    #选择照片
    select_photos = (By.XPATH,'//*[@resource-id="com.yiqizhangda.teacher:id/recyclerview"]/android.widget.FrameLayout[1]/android.view.View')

    #选择照片确定
    select_photos_but =(By.ID,'com.yiqizhangda.teacher:id/button_apply')

    #标题
    title_text = (By.ID,'com.yiqizhangda.teacher:id/publish_title_edit')

    #内容
    content_text = (By.ID,'com.yiqizhangda.teacher:id/publish_content_edit')

    #下一步按钮
    next_but = (By.ID,'com.yiqizhangda.teacher:id/next')

    #发布按钮
    publish_but = (By.ID,'com.yiqizhangda.teacher:id/publish_action')

    #进入案例库
    library = (By.ID,'com.yiqizhangda.teacher:id/look_example')

    #选择主题
    select_topic = (By.ID,'com.yiqizhangda.teacher:id/subject_layout')

    #选择主题页面确定
    topic_but =(By.ID,'com.yiqizhangda.teacher:id/next')

    #选择发布方式页面
    select_publish_type = (By.ID,'com.yiqizhangda.teacher:id/type_layout')

    #指定发送
    specified_send = (By.XPATH,'//*[@resource-id = "com.yiqizhangda.teacher:id/type_list"]/android.view.View[2]')

    #指定发送确定
    specified_send_button = (By.ID,'com.yiqizhangda.teacher:id/next')

    def __init__(self, driver):
        super().__init__(driver)
        self.Common = Common(driver)
        self.checkPopup = CheckPopup(driver)
        self.checkPublishGarden = CheckGarden(driver)

    def album_choice(self,num):
        """
        相册页面选择照片
        :param num:
        :return:
        """
        try:
            for i in range(1,int(num+1)):
                self.driver.find_element(By.XPATH,'//*[@resource-id="com.yiqizhangda.teacher:id/recyclerview"]/'
                                                  'android.widget.FrameLayout[{}]/'
                                                  'android.view.View'.format(i)).click()
        except NoSuchElementException as msg:
            logging.error("未找到该元素")
            return False

    def choice_pic(self, num):
        """
        选择照片并确定
        :param title:
        :param content:
        :param num:
        :return:
        """
        logging.info("点击首页发布")
        self.driver.find_element(*self.publish_button).click()
        logging.info("选择发布方式为“【在园时光】”")
        self.driver.find_element(*self.publish_garden).click()
        logging.info("进入相册，选择发布照片")
        self.album_choice(num)
        logging.info("选择了%s照片后，点击【确定】" %num)
        self.driver.find_element(*self.select_photos_but).click()

    def input_title(self,title):
        """
        输入标题
        :param title:
        :return:
        """
        logging.info("输入标题：%s" % title)
        self.driver.find_element(*self.title_text).send_keys(title)

    def input_content(self, content):
        """
        输入内容
        :param content:
        :return:
        """
        logging.info("输入发布内容：%s" % content)
        self.driver.find_element(*self.content_text).send_keys(content)

    def next_step(self):
        """
        下一步
        :return:
        """
        logging.info("点击【下一步】")
        self.driver.find_element(*self.next_but).click()

    def choice_library(self,first_title,second_title):
        """
        选择文本范例库
        :param first_title:
        :param second_title:
        :param num:
        :return:
        """
        logging.info('选择活动范例')
        self.driver.find_element(*self.library).click()
        logging.info("选择第%s个大标题" %first_title)
        self.driver.find_element(By.XPATH,"//*[@resource-id='com.yiqizhangda.teacher:id/level_1_tab']/"
                                          "android.widget.LinearLayout/"
                                          "android.widget.RelativeLayout[{}]".format(first_title)).click()
        logging.info("选择第%s个小标题" %second_title)
        self.driver.find_element(By.XPATH,"//*[@resource-id='com.yiqizhangda.teacher:id/example_tab']/"
                                          "android.widget.LinearLayout/"
                                          "android.widget.RelativeLayout[{}]".format(second_title)).click()
        logging.info("默认选择第一条")
        self.driver.find_element(By.XPATH,"//*[@resource-id='com.yiqizhangda.teacher:id/example_list']/"
                                          "android.view.View[1]/android.widget.TextView[2]").click()

    def select_gudren_topic(self,num):
        """
        选择主题
        :param num:
        :return:
        """
        logging.info("进入选择“主题”")
        self.driver.find_element(*self.select_topic).click()
        try:
            logging.info("选择第%s个主题" %num)
            self.driver.find_element(By.XPATH,'//*[@resource-id	= "com.yiqizhangda.teacher:id/subject_list"]/'
                                              'android.view.View[{}]'.format(num+1))
        except NoSuchElementException as msg:
            self.driver.find_element(By.XPATH,'//*[@resource-id	= "com.yiqizhangda.teacher:id/subject_list"]/'
                                              'android.view.View[1]').click()
        else:
            self.driver.find_element(By.XPATH,'//*[@resource-id	= "com.yiqizhangda.teacher:id/subject_list"]/'
                                              'android.view.View[{}]'.format(num + 1)).click()
        logging.info("选择完成之后点击【确定】")
        self.driver.find_element(*self.topic_but).click()

    def select_gudren_publish_type(self,kid_num):
        """
        指定发送
        :param kid_num:
        :return:
        """
        logging.info("进入选择发布方式页面")
        self.driver.find_element(*self.select_publish_type).click()
        logging.info("选择“指定发送”")
        self.driver.find_element(*self.specified_send).click()
        logging.info('选择指定%s个孩子' %kid_num)
        try:
            for i in range(1,int(kid_num+1)):
                self.driver.find_element(By.XPATH,'//*[@resource-id = "com.yiqizhangda.teacher:id/kid_list"]/'
                                                  'android.widget.RelativeLayout[{}]'.format(i)).click()
        except NoSuchElementException as msg:
            logging.error("该班级没有孩子可供选择")
            return False
        logging.info("点击【确定】按钮")
        self.driver.find_element(*self.specified_send_button).click()

    def publish_garden_button(self):
        """发布按钮"""
        logging.info("点击【发布】在园时光")
        self.driver.find_element(*self.publish_but).click()

    def check_success(self,title):
        """
        校验发布
        :param title:
        :return:
        """
        logging.info("检测成长册是否发送成功")
        try :
            sleep(3)
            self.driver.find_element(By.XPATH,"//android.widget.TextView[contains(@text," + "'" + title + "'" + ")]")
        except NoSuchElementException:
            logging.error('发布失败!')
            self.getScreenShot('发布失败')
            return False
        else:
            logging.info('发布成功!')
            return True



if __name__=="__main__":
    driver = appium_desired()
    l =PublishPic(driver)
    l.checkPopup.check_slide()
    l.checkPopup.check_window()
    l.choice_pic(4,"马文涛")
    l.choice_library('2','2')
    l.input_title("测试")
    l.next_step()
    l.select_gudren_topic(1)
    l.select_gudren_publish_type(3)
    l.publish_garden_button()
    l.checkPublishGarden.check_publish_success("22")
    #l.check_success('sda')


