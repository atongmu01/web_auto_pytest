#Author: Xqq


class Login_Page_Location:
    # 手机号输入框
    login_username_xpath="//input[@name='phone']"
    # 密码输入框
    login_password_xpath = "//input[@name='password']"
    # 登录按钮
    login_button_xpath = "//button[@class='btn btn-special']"
    #登录区域--错误提示信息
    errormsg_from_loginArea_xpath="//div[@class='form-error-info']"
    account_password_error_xpath="//div[@class='layui-layer-content']"
