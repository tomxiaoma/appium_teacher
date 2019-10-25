from baseView.baseView import BaseView
import logging
import time,os
import csv


class Common(BaseView):

    #获取屏幕尺寸
    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    #滑动
    def swipeLeft(self):
        l = self.get_size()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    #获取时间
    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    #获取截图方法
    def getScreenShot(self,module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)

    #获取CSV数据，做数据驱动
    def get_csv_data(self,csv_file,line):
        logging.info('=====获取CSV文件中的数据======')
        with open(csv_file) as file:
            reader = csv.reader(file)
            for index,row in enumerate(reader,1):
                if index == line:
                    return row








