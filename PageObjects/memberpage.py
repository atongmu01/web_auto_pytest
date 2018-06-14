#Author: Xqq
from WEB_Framework_V1.PageLocations.member_page_locatin import Member_Page_Location as MP
from WEB_Framework_V1.PageObjects.basepage import BasePage


class MemberPage(MP,BasePage):

    def get_balance(self):
        self.wait_eleLocated(self.balance_xpath)
        return self.driver.find_element_by_xpath(self.balance_xpath).text