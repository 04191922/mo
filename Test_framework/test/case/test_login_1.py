import os
import time
import psutil
import unittest  # 单元测试模块
from selenium import webdriver  # 引入浏览器驱动
from selenium.webdriver.common.by import By  # 引入xpath查找模块
from browser import Browser
from digital_home import DigitalHomeLogin
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH  # 引入配置
from utils.log import logger  # 引入日志模块
from utils.file_reader import ExcelReader  # 引入xls读取模块
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from page.baidu_result_page import BaiDuMainPage, BaiDuResultPage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase):
    URL = Config().get('test_url')

    #excel = DATA_PATH + '\\baidu.xls'

    @classmethod
    def setUpClass(cls):
        cls.driver = Browser(browser_type='chrome').get(cls.URL, maximize_window=False)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def login(self):
        # 定位登录按钮，打开登录窗
        self.page = DigitalHomeLogin(self.driver)  # 使用已经打开的浏览器实例
        loginbotton = self.page.search()
        time.sleep(4)
        # 定位手机号输入框13428826815
        # 输入手机号
        phone = self.page.inputphonenum('13428826815')
        time.sleep(1)
        vrcode = self.page.inputver('123456')
        result = self.page.login1()
        print(f"login result:{result}")
        return result

    def test_login(self):

            result = self.login()

            print(f"login method:{result}")
            self.assertEqual(result,'登录成功')



if __name__ == '__main__':

    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='墨镜', description='修改html报告')
        unittest.main(testRunner=runner)

