import unittest

from hello.py import sayHello

class testHello(unittest.testCase):
  def test_sayHello(self):
    self.assertEqual(sayHello(), "Hello World")
    
if __name__ == '__main__':
  unittest.main()