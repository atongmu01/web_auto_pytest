# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 15:47
# @Author  : XQQ
# @File    : main_pytest.py
# @Software: PyCharm Community Edition
import pytest

# -q 不显示版本配置信息  -m mark标记
pytest.main(["-q","-m","smoke","--html=TestReport\pytest_report.html","--junitxml=TestReport\pytest_report.xml","TestCases"])