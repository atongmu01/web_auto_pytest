#Author: Xqq
import unittest
import pytest
from selenium import webdriver
from WEB_Framework_V1.PageObjects.loginpage import LoginPage
from WEB_Framework_V1.PageObjects.loanpage import LoanPage
from WEB_Framework_V1.PageObjects.homepage import HomePage
from WEB_Framework_V1.PageObjects.memberpage import MemberPage
from WEB_Framework_V1.TestDatas.invest_testdata import *
from WEB_Framework_V1.TestDatas.common_data import *

@pytest.mark.usefixtures("init_invest")
class Test_Invest():

    #投资成功用例
    @pytest.mark.smoke
    def test_invest_ok(self,init_invest):
        money=invest_ok_data["money"]
        check_msg=invest_ok_data["check_msg"]

        # 跳转到投标页面
        hp = HomePage(init_invest)
        hp.click_invest_jump()
        #获取投资前余额
        loanpage = LoanPage(init_invest)
        old_balance=float(loanpage.get_balance().strip("元"))
        #输入投资金额
        loanpage.input_invest_money(money)
        #点击投标按钮
        loanpage.click_invest_button()
        #获取成功信息与期望对比
        assert check_msg in loanpage.get_invest_ok()
        #点击激活按钮
        loanpage.click_active_button()
        #获取投资后的余额
        mp = MemberPage(init_invest)
        new_balance=float(mp.get_balance().strip("元"))
        #投资前后余额对比
        assert int(old_balance-new_balance)==money

    #投资非100整数倍用例
    def test_invest_fail_no100(self,init_invest):
        money=invest_fail_no100_data["money"]
        check_msg=invest_fail_no100_data["check_msg"]


        #跳转到投标页面
        hp = HomePage(init_invest)
        hp.click_invest_jump()
        #获取投资前余额
        loanpage = LoanPage(init_invest)
        old_balance=float(loanpage.get_balance().strip("元"))
        #输入投资金额
        loanpage.input_invest_money(money)
        #点击投标按钮
        loanpage.click_invest_button()
        #获取失败信息与期望对比
        assert check_msg in loanpage.get_invest_error()
        #失败后点击确认按钮
        loanpage.click_confirm_button()
        #获取投资后的余额
        new_balance=float(loanpage.get_balance().strip("元"))
        #投资前后余额对比
        assert new_balance==old_balance

