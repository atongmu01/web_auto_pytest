#Author: Xqq
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self,driver):
        self.driver=driver

    #等待元素加载
    def wait_eleLocated(self,location,by=By.XPATH,wait=20,frequnce=0.5):
        if by not in By.__dict__.values():
            print("定位类型不支持，请更换成selenium支持的定位方式!")
            raise Exception
        WebDriverWait(self.driver, wait, frequnce).until(EC.presence_of_element_located((by, location)))

    #查找一个元素
    def get_element(self,location,by=By.XPATH,wait=20,frequnce=0.5):
        #等待元素加载
        self.wait_eleLocated(location,by,wait,frequnce)
        #查找元素
        return self.driver.find_element(by,location)

     # 查找多个元素
    def get_elements(self, location, by=By.XPATH, wait=20, frequnce=0.5):
        # 等待元素加载
        self.wait_eleLocated(location, by, wait, frequnce)
        # 查找元素
        return self.driver.find_elements(by, location)

    # 滚动元素到可见区域
    def scroll_ele_intoView(self,ele):
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

