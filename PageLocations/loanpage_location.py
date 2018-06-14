# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 16:04
# @Author  : XQQ
# @File    : loan_page_location.py
# @Software: PyCharm Community Edition

class Loan_Page_Location:
    # 投资金额(及查询余额)
    invest_money_xpath = "//div[@class='right']//div[@class='clearfix left']//input"
    # 投标按钮
    invest_button_xpath = "//button[text()='投标']"
    # 投资成功弹出框 查看并激活按钮
    invest_success_activeButton_xpath="//div[@class='layui-layer-content']//button"
    # 投资成功弹出框，获取投资成功信息
    get_invest_ok_xpath="//div[@class='layui-layer-content']//div[@class='capital_font1 note']"
    #投资失败弹出框，获取失败信息
    invest_failed_xpath="//div[contains(@class,'layui-layer-dialog')]//div[@class='text-center']"
    #投资失败弹出框，确认按钮
    invest_failed_confirmButton_xpath="//div[contains(@class,'layui-layer-dialog')]//a[text()='确认']"