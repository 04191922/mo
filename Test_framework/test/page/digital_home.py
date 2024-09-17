from selenium.webdriver.common.by import By

from common.page import Page


class DigitalHomeLogin(Page):

    # login_btn = (By.CLASS_NAME, 'login-btn')
    # phone_input =(By.CLASS_NAME,'arco-input arco-input-size-medium')
    # verification_code = (By.CSS_SELECTOR,'#code > div.arco-form-item-content-wrapper > div > div > span > input')

    login_btn = (By.CLASS_NAME, 'login-btn')
    phone_input = (By.CSS_SELECTOR, '.arco-input.arco-input-size-medium')  # 修正选择器
    verification_code = (By.CSS_SELECTOR,'#code > div.arco-form-item-content-wrapper > div > div > span > input')

    def search(self):

        self.find_element(*self.login_btn).click()  # 寻找搜索按钮后点击按钮

    def inputphonenum(self,kw):
        phone_input_elem = self.find_element(*self.phone_input)  # 寻找手机号输入框
        phone_input_elem.click()
        phone_input_elem.send_keys(kw)  # 输入手机号


    def inputver(self,kw):
        verification_code_elem = self.find_element(*self.verification_code)  # 寻找验证码输入框
        verification_code_elem.send_keys(kw)  # 输入验证码