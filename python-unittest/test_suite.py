import unittest

from test_baidu import TestBaiDu
from test_mathfunc import TestMathFunc
from HTMLTestRunner import HTMLTestRunner
if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide"), TestBaiDu("test_baidu")]   # 添加测试用例列表
    suite.addTests(tests)   # 将测试用例列表添加到测试组中
    suite.addTest(TestMathFunc("test_multi"))  # 直接用addTest方法添加单个TestCase
    # 用addTests + TestLoader。不过用TestLoader的方法是无法对case进行排序的
    # loadTestsFromName()，传入'模块名.TestCase名'
    suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))  # loadTestsFromNames()，类似，传入列表

    # loadTestsFromTestCase()，传入TestCase
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    # suite中也可以套suite

    # 将测试结果输出到测试报告中
    # with open('UnittestTextReport.txt', 'a') as f:
    #     runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #     runner.run(suite)

    # 将测试结果输出到测试报告html中
    with open('HTMLReport.html', 'w') as f:
        runner = HTMLTestRunner(stream=f,
                                title='MathFunc Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        # runner = BeautifulReportRunner(stream=f,
        #                                description='测试报告描述',
        #                                title='测试报告标题',
        #                                verbosity=2)
        runner.run(suite)

    # 直接将结果输出到控制台
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)