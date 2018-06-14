#Author: Xqq
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from WEB_Framework_V1.PageLocations.homepage_location import Home_Page_Location as HP
from WEB_Framework_V1.PageObjects.basepage import BasePage


class HomePage(HP,BasePage):

    def get_user_nickname(self):
        self.wait_eleLocated(self.nickname)
        return self.driver.find_element_by_xpath(self.nickname).text

    def click_invest_jump(self):
        eles=self.get_elements(self.jump_loanpage_xpath)
        index=random.randint(0,len(eles)-1)
        eles[index].click()

