import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.service import Service as IEService
from utils.config import DRIVER_PATH, REPORT_PATH

CHROMEDRIVER_PATH = DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie}
EXECUTABLE_PATH = {'firefox': None, 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH}

class UnSupportBrowserTypeError(Exception):
    pass

class Browser(object):
    def __init__(self, browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get(self, url, maximize_window=True, implicitly_wait=30):
        if self._type == 'chrome':
            options = ChromeOptions()
            #options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            service = Service(executable_path=EXECUTABLE_PATH[self._type])
            self.driver = self.browser(service=service, options=options)
        elif self._type == 'firefox':
            options = FirefoxOptions()
           # options.add_argument("--headless")
            service = FirefoxService(executable_path=EXECUTABLE_PATH[self._type])
            self.driver = self.browser(service=service, options = options)
        elif self._type == 'ie':
            service = IEService(executable_path=EXECUTABLE_PATH[self._type])
            self.driver = self.browser(service=service)
        else:
            raise UnSupportBrowserTypeError('不支持的浏览器类型！')

        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        #screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        #save_screen_shot方法中使用os.path.join来拼接路径，这可以使代码更加跨平台兼容
        screenshot_path = os.path.join(REPORT_PATH, 'screenshot_%s' % day)
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

# 这里试验了一下保存截图的方法，保存png截图到report目录下。
if __name__ == '__main__':
    b = Browser('chrome').get('http://www.baidu.com')
    b.save_screen_shot('test_baidu')
    time.sleep(3)
    b.quit()
