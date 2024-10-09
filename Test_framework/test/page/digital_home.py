import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test.common.page import Page

class DigitalHomeLogin(Page):

    #登录按钮
    login_btn = (By.CLASS_NAME, 'login-btn')
    #手机号输入框
    phone_input =(By.CSS_SELECTOR,'#phone > div > div > div > span > input')
    #获取验证码
    get_vercode_btn = (By.CLASS_NAME,'code-btn')
    #验证码输入框
    verification_code = (By.CSS_SELECTOR,'#code > div.arco-form-item-content-wrapper > div > div > span > input')
    #隐私勾选
    agreement_select = (By.CLASS_NAME,'agreement-select')
    #弹窗定位
    popup_selector = (By.CLASS_NAME, 'login-box-right')
    # el-id-996-7 > div > div > div.phone-login > div.login-btn

    def wait_for_popup(self):#定位弹窗
        # 等待弹窗出现
        wait = WebDriverWait(self.driver, 10)
        popup = wait.until(EC.visibility_of_element_located(self.popup_selector))
        return popup
    def search(self):
        self.find_element(*self.login_btn).click()  # 寻找登录按钮后点击按钮

    #手机号输入
    def inputphonenum(self,kw):
        time.sleep(1)
        self.find_element(*self.phone_input).click()
        time.sleep(1)
        self.find_element(*self.phone_input).send_keys(kw)#输入手机号

    def login(self):
        popup = self.wait_for_popup()
        login_button_inside_popup = popup.find_element(*self.login_btn)
        self.find_element(*self.agreement_select).click()
        time.sleep(1)
        login_button_inside_popup.click()
        time.sleep(5)
        # 定位所有登录按钮并找到显示的那个
        #login_button_inside_popup = next(btn for btn in login_buttons if btn.is_displayed())
        # 点击协议选择框
        # self.find_element(*self.agreement_select).click()
        # time.sleep(1)
        # # 点击显示的登录按钮
        # self.find_element(*self.login_btn1).click()

    def inputver(self,kw):
        self.find_element(*self.get_vercode_btn).click() #点输入验证码按钮
        time.sleep(0.1)
        self.find_element(*self.verification_code).send_keys(kw)#输入验证码


