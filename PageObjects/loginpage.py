#Author: Xqq
import time
import unittest
from selenium import webdriver
from WEB_Framework_V1.PageLocations.loginpage_location import Login_Page_Location as LP
from WEB_Framework_V1.PageObjects.basepage import BasePage

class LoginPage(LP,BasePage):


    def login(self,url,username,password):
        self.driver.get(url)
        self.wait_eleLocated(self.login_username_xpath)
        self.driver.find_element_by_xpath(self.login_username_xpath).send_keys(username)
        self.driver.find_element_by_xpath(self.login_password_xpath).send_keys(password)
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    #获取登录区域的错误信息
    def get_errorMsg_from_loginArea(self):
        self.wait_eleLocated(self.errormsg_from_loginArea_xpath)
        return self.driver.find_element_by_xpath(self.errormsg_from_loginArea_xpath).text

    #帐号或密码错误的错误信息
    def get_account_password_error(self):
        self.wait_eleLocated(self.account_password_error_xpath)
        return self.driver.find_element_by_xpath(self.account_password_error_xpath).text


