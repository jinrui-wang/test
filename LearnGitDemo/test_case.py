'''
1.创建一个类 继承unittest.TestCase类 ---unit单元test测试(python里面的单元测试框架) TestCase(测试用例类)
2.编写初始化setUp函数 和测试结束tearDown的函数
3.根据测试用例 编写各个测试用例函数 ---->必须以test开头
4.main函数中执行单元测试
导包unittest:
    1.加上unittest. 按alt+enter键进行导包
    2.pycharm关联的python环境有问题
        file-->setting-->project...-->project intercepter-->下拉框选择自己安装的那个python.exe-->OK


'''
import unittest
#1.创建一个类 继承unittest.TestCase类 ---unit单元test测试(python里面的单元测试框架) TestCase(测试用例类)
from zidonghua.jiSuanQi import jiSuanQi


class TestJsq(unittest.TestCase):
    def setUp(self):
        print('初始化函数')

    # 3.根据测试用例 编写各个测试用例函数 ---->必须以test开头
    # 1 2,3     -2 100,98
    def test_01_add(self):
        print('01')

        jsq = jiSuanQi()
        # 调用加法函数 获取实际结果
        result = jsq.add(1,2)

        # 断言判断 预期结果 和 实际结果...assertEqual()判断预期结果和实际结果是否一致
        self.assertEqual(3,result)

    def test_02_add(self):
        print('02')
        jsq = jiSuanQi()
        result = jsq.add(-2,100)

        self.assertEqual(98,result)

    # 多个数相加 1 2 3 4 5 6 7 8 9,45
    def test_03_addMore(self):
        print('03')
        jsq = jiSuanQi()

        result = jsq.addMore(1,2,3,4,5,6,7,8,9)

        self.assertEqual(45,result)


    def tearDown(self):
        print('结束函数')

# No没有 tests测试用例函数 were found找到

if __name__ == '__main__':
    # 4.main函数中执行单元测试
    unittest.main()


















