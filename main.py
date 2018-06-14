#Author: Xqq
import os
import time
import unittest
import HTMLTestRunner

suite = unittest.TestSuite()

testcase_dir = os.getcwd() + "/TestCases"
testreport_dir = os.getcwd() + "/TestReport"

suite.addTests(unittest.TestLoader().discover(testcase_dir))

#取当前时间
now=time.strftime('%Y-%m-%d_%H_%M_%S')
f= open(testreport_dir+"//"+now+'Web_Auto_report.html','wb')
runner=HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title='接口测试报告',
    description='用例执行情况',
    verbosity = 2
)


if __name__=='__main__':
    runner.run(suite)
    f.close()