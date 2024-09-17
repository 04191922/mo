import os
import time
import psutil
import unittest  # 单元测试模块

import requests
from selenium import webdriver  # 引入浏览器驱动
from selenium.webdriver.common.by import By  # 引入xpath查找模块
from common.browser import Browser
from digital_home import DigitalHomeLogin
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH  # 引入配置
from utils.log import logger  # 引入日志模块
from utils.file_reader import ExcelReader  # 引入xls读取模块
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from page.baidu_result_page import BaiDuMainPage, BaiDuResultPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin(unittest.TestCase):
    URL = Config().get('local_url')

    #excel = DATA_PATH + '\\baidu.xls'

    @classmethod
    def setUpClass(cls):
        cls.driver = Browser(browser_type='chrome').get(cls.URL, maximize_window=False)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        # 定位登录按钮，打开登录窗
        self.page = DigitalHomeLogin(self.driver)  # 使用已经打开的浏览器实例
        loginbotton =self.page.search()
        time.sleep(2)
        print(loginbotton)
        #定位手机号输入框
        # 输入手机号
        phone = self.page.inputphonenum('13168310924')
        print(phone)
        time.sleep(1)
        #调第三方接口发送请求
        verification_code = self.get_verification_code('13168310924')
        print(f'获取到的验证码是: {verification_code}')

        #调用验证码接口获取验证码
        #定位验证码输入框，获取正确验证码填入验证码输入框
        self.page.inputver(verification_code)
        #定位登录/注册按钮点击确定
        #设置断言


    def get_verification_code(self, phone_number):
        # 第三方接口URL
        url = 'https://api.example.com/get_verification_code'
        # 请求参数，根据实际情况进行调整
        params = {
            'phone': phone_number
        }
        # 发送GET请求
        response = requests.get(url, params=params)
        # 检查响应状态码
        if response.status_code == 200:
            # 假设返回的JSON响应中包含验证码
            return response.json().get('verification_code')
        else:
            # 处理错误情况
            response.raise_for_status()




if __name__ == '__main__':

    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='墨镜', description='修改html报告')
        unittest.main(testRunner=runner)
    # 计算运行时间差

