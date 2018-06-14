#Author: Xqq
import time
from WEB_Framework_V1.PageLocations.loanpage_location import Loan_Page_Location as LP
from WEB_Framework_V1.PageObjects.basepage import BasePage


class LoanPage(LP,BasePage):


    def get_balance(self):
        ele=self.get_element(self.invest_money_xpath)
        self.scroll_ele_intoView(ele)
        return ele.get_attribute("data-amount")

    def input_invest_money(self,money):
        ele = self.get_element(self.invest_money_xpath)
        self.scroll_ele_intoView(ele)
        ele.send_keys(money)

    def click_invest_button(self):
        ele = self.get_element(self.invest_button_xpath)
        self.scroll_ele_intoView(ele)
        ele.click()

    def get_invest_ok(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath(self.get_invest_ok_xpath).text

    def click_active_button(self):
        self.wait_eleLocated(self.invest_success_activeButton_xpath)
        self.driver.find_element_by_xpath(self.invest_success_activeButton_xpath).click()

    def get_invest_error(self):
        time.sleep(2)
        return self.driver.find_element_by_xpath(self.invest_failed_xpath).text

    def click_confirm_button(self):
        self.wait_eleLocated(self.invest_failed_confirmButton_xpath)
        self.driver.find_element_by_xpath(self.invest_failed_confirmButton_xpath).click()