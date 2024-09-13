from selenium.webdriver.common.by import By
from test.common.page import Page

class DigitalHomeLogin(Page):

    login_btn = (By.CLASS_NAME, 'login-btn')
    phone_input =(By.CLASS_NAME,'arco-input arco-input-size-medium')
    verification_code = (By.CSS_SELECTOR,'#code > div.arco-form-item-content-wrapper > div > div > span > input')
    def search(self):

        self.find_element(*self.login_btn).click()  # 寻找搜索按钮后点击按钮

    def inputphonenum(self,kw):
        self.find_element(*self.phone_input).click()
        self.find_element(*self.phone_input).send_keys(kw)#输入手机号

    def inputver(self,kw):
        self.find_element(*self.verification_code).send_keys(kw)#输入验证码