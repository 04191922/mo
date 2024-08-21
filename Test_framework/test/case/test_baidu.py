import os
import time
import psutil
import unittest  # 单元测试模块
from selenium import webdriver  # 引入浏览器驱动
from selenium.webdriver.common.by import By  # 引入xpath查找模块
from browser import Browser
from utils.config import Config, DRIVER_PATH, DATA_PATH, REPORT_PATH  # 引入配置
from utils.log import logger # 引入日志模块
from utils.file_reader import ExcelReader  # 引入xls读取模块
from utils.HTMLTestRunner import HTMLTestRunner
from utils.mail import Email
from page.baidu_result_page import BaiDuMainPage, BaiDuResultPage
class TestBaiDu(unittest.TestCase):
    URL = Config().get('URL')
    excel = DATA_PATH + '\\baidu.xls'

    @classmethod
    def setUpClass(cls):
        cls.driver = Browser(browser_type='chrome').get(cls.URL, maximize_window=False)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_search(self):
        # 打印文件路径以确认
        print(f"Excel 文件路径: {self.excel}")
        start_time = time.time()
        # 确认 self.excel 是否确实指向一个文件
        if not os.path.isfile(self.excel):
            raise FileNotFoundError(f"指定的路径不是一个文件: {self.excel}")

        # 尝试读取文件
        try:
            datas = ExcelReader(self.excel).data
        except PermissionError as e:
            print(f"权限错误：{e}")
            # 检查文件和目录权限，确保脚本有读取权限
        except FileNotFoundError as e:
            print(f"文件不存在错误：{e}")

        for d in datas:
            with self.subTest(data=d):
                self.start_cpu_time = time.process_time()
                self.page = BaiDuMainPage(self.driver)  # 使用已经打开的浏览器实例
                self.page.search(d['search'])
                time.sleep(2)
                self.page = BaiDuResultPage(self.page)  # 页面跳转到result page
                links = self.page.result_links
                for link in links:
                    logger.info(link.text)
                    print("ceshi")
                self.end_cpu_time = time.process_time()
                cpu_time = self.end_cpu_time - self.start_cpu_time
                print(f"CPU时间: {cpu_time} 秒")
                # 获取当前进程的CPU占用率
                process = psutil.Process(os.getpid())
                mem_info = process.memory_info()
                cpu_usage = process.cpu_percent(interval=1)  # 间隔1秒获取CPU占用率
                print(f"进程实际使用的物理内存大小: {mem_info.rss} KB")
                print(f"进程使用的虚拟内存大小: {mem_info.vms} KB")
                print(f"CPU占用率: {cpu_usage}%")
                end_time = time.time()
                # 计算运行时间差
                total_time = end_time - start_time
                print(f"运行时间: {total_time} 秒")

if __name__ == '__main__':
    start_time = time.time()
    report = REPORT_PATH + '\\report.html'
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='墨镜', description='修改html报告')
        unittest.main(testRunner=runner)
    end_time = time.time()
    # 计算运行时间差
    total_time = end_time - start_time
    print(f"运行时间: {total_time} 秒")


#     URL = Config().get('URL')
#     excel = DATA_PATH + '\\baidu.xls'
#
#
#     def sub_setUp(self):
#         # 初始页面是main page，传入浏览器类型打开浏览器
#         self.page = Browser(browser_type='chrome').get(self.URL, maximize_window=False)
#
#    # cls.driver = Browser(browser_type='chrome').get(cls.URL, maximize_window=False)
#     def sub_tearDown(self):
#         self.driver.quit()  # 清理退出
#
#     def test_search(self):
#         # 打印文件路径以确认
#         print(f"Excel 文件路径: {self.excel}")
#
#         # 确认 self.excel 是否确实指向一个文件
#         if not os.path.isfile(self.excel):
#             raise FileNotFoundError(f"指定的路径不是一个文件: {self.excel}")
#
#         # 尝试读取文件
#         try:
#             datas = ExcelReader(self.excel).data
#         except PermissionError as e:
#             print(f"权限错误：{e}")
#             # 检查文件和目录权限，确保脚本有读取权限
#         except FileNotFoundError as e:
#             print(f"文件不存在错误：{e}")
#        # datas = ExcelReader(self.excel).data
#         for d in datas:
#             with self.subTest(data=d):
#                 self.sub_setUp()
#                 self.page.search(d['search'])
#                 time.sleep(2)
#                 self.page = BaiDuResultPage(self.page)  # 页面跳转到result page
#                 links = self.page.result_links
#                 for link in links:
#                     logger.info(link.text)
#                 self.sub_tearDown()
#
# if __name__ == '__main__':
#     # unittest.main()
#
#     report = REPORT_PATH + '\\report.html'
#     print(report)
#     with open(report, 'wb') as f:
#         runner = HTMLTestRunner(f, verbosity=2, title='栾鹏全栈', description='修改html报告')
#         runner.run(TestBaiDu('test_search'))
#
#     # e = Email(title='百度搜索测试报告',
#     #           message='这是今天的测试报告，请查收！',
#     #           receiver='...',
#     #           server='...',
#     #           sender='...',
#     #           password='...',
#     #           path=report
#     #           )
#     # e.send()