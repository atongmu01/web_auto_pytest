# -*- coding: utf-8 -*-
# @Time    : 2018/6/8 13:58
# @Author  : XQQ
# @File    : conftest.py
# @Software: PyCharm Community Edition
import pytest
from selenium import webdriver
from WEB_Framework_V1.PageObjects.loginpage import LoginPage
from WEB_Framework_V1.TestDatas.invest_testdata import *
from WEB_Framework_V1.TestDatas.common_data import *

@pytest.fixture()
def init_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture()
def init_invest():
    driver = webdriver.Chrome()
    driver.maximize_window()
    username = invest_ok_data["username"]
    password = invest_ok_data["password"]
    LoginPage(driver).login(url,username,password)
    yield driver
    driver.close()
    driver.quit()