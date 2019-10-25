from common.myunit import StartEnd
from businessView.publish_garden.publishGradenView import PublishPic
from businessView.publish_garden.checkPublishGarden import CheckGarden
import unittest
import logging


class TestPublish(StartEnd):

    def test_publish_all(self):
        logging.info('===============【在园时光】全部发送在园时光===============')
        l = PublishPic(self.driver)
        l.checkPopup.check_slide()
        l.checkPopup.check_window()
        l.choice_pic(4, "马文涛")
        l.input_title("测试")
        l.input_content("内容测试")
        l.next_step()
        l.publish_garden_button()
        self.assertTrue(l.checkPublishGarden.check_publish_success("测试"))

    def test_publish_appoint(self):
        logging.info('===============【在园时光】指定发送在园时光===============')
        l = PublishPic(self.driver)
        l.checkPopup.check_slide()
        l.checkPopup.check_window()
        l.choice_pic(4, "马文涛")
        l.input_title("测试")
        l.input_content("内容测试")
        l.next_step()
        l.select_gudren_publish_type(2)
        l.publish_garden_button()

    def test_publish_topic(self):
        logging.info('===============【在园时光】选择主题发送在园时光===============')
        l = PublishPic(self.driver)
        l.checkPopup.check_slide()
        l.checkPopup.check_window()
        l.choice_pic(4, "马文涛")
        l.input_title("测试")
        l.input_content("内容测试")
        l.next_step()
        l.select_gudren_topic(1)
        l.publish_garden_button()

    def test_publish_case(self):
        logging.info('===============【在园时光】选择案例描述发送在园时光===============')
        l = PublishPic(self.driver)
        l.checkPopup.check_slide()
        l.checkPopup.check_window()
        l.choice_pic(4, "马文涛")
        l.choice_library('2', '2')
        l.input_title("测试")
        l.next_step()
        l.publish_garden_button()


if __name__ == '__main__':
    unittest.main()