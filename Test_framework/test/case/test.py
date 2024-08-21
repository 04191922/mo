from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
if __name__ == '__main__':
# 确保chromedriver路径设置正确，如果未设置，需要提供完整的chromedriver路径,我的配置不生效！！！！！麻了
    service = Service('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    driver = webdriver.Chrome(service=service)# selenium4以上版本，打开浏览器方法需要sevice代替，如果chromedriver在PATH中，可以直接这样使用
#driver = webdriver.Chrome()
# 如果chromedriver不在PATH中，需要提供完整的chromedriver路径
# driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
# 访问一个网页

    driver.get('https://www.example.com')
# 等待页面加载完成
# ...
# 关闭浏览器
    time.sleep(3)
    driver.quit()
    print(webdriver.__version__)