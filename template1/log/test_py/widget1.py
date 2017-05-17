#coding:utf-8
# from widget import Widget
import unittest
class Widget():
    def __init__(self, size = (40, 40)):
        self._size = size
    def getSize(self):
        return self._size
    def resize(self, width, height):
        if width < 0 or height < 0:
            raise ValueError, "illegal size"
            self._size = (width, height)
    def dispose(self):
        pass

#一个一个执行的
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(WidgetTestCase("testSize"))
#     suite.addTest(WidgetTestCase("testResize"))
#     return suite
#执行该类下的所有test的用例
def suite():
    return unittest.makeSuite(WidgetTestCase, "test")



class WidgetTestCase(unittest.TestCase):
    # 测试 getSize()方法的测试用例
    # self.assertEqual(self.widget.getSize(), (40, 40))
    # 测试 resize()方法的测试用例
    def setUp(self):
        self.widget = Widget()
    def tearDown(self):
        self.widget.dispose()
        self.widget = None
    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))
    def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))
    # 测试
if __name__ == "__main__":
    unittest.main(defaultTest='suite')