#Author: Xqq
import unittest
import pytest
import time
from selenium import webdriver
from WEB_Framework_V1.PageObjects.loginpage import LoginPage
from WEB_Framework_V1.PageObjects.homepage import HomePage
from WEB_Framework_V1.TestDatas.login_testdata import *
from WEB_Framework_V1.TestDatas.common_data import *

@pytest.mark.uesfixtures("init_login")
@pytest.mark.login
class Test_Login():

    #登录没有密码用例
    @pytest.mark.smoke
    def test_login_noPassword(self,init_login):
        username=login_noPassword_data["username"]
        password=login_noPassword_data["password"]
        check_msg=login_noPassword_data["check_msg"]

        #执行login
        lp = LoginPage(init_login)
        lp.login(url,username,password)

        #期望结果与实际结果比对
        assert lp.get_errorMsg_from_loginArea()==check_msg


    #登录密码错误用例
    def test_login_errorPassword(self,init_login):
        username = login_errorPassword_data["username"]
        password = login_errorPassword_data["password"]
        check_msg = login_errorPassword_data["check_msg"]

        #执行login
        lp = LoginPage(init_login)
        lp.login(url,username,password)

        #期望结果与实际结果比对
        assert lp.get_account_password_error()==check_msg


    #登录正确用例
    @pytest.mark.smoke
    def test_login_ok(self,init_login):
        username = login_ok_data["username"]
        password = login_ok_data["password"]
        check_msg = login_ok_data["check_msg"]

        #执行login
        lp = LoginPage(init_login)
        lp.login(url,username,password)

        #期望结果与实际结果比对
        hp = HomePage(init_login)
        assert hp.get_user_nickname()==check_msg
