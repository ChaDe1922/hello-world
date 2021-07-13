import unittest

from hello.py import sayHello

class TestFileName(unittest.testCase):
  def test_sayHello(self):
    greeting = sayHello()
    self.assertEqual(greeting, "Hello World")
    
if __name__ == '__main__':
  unittest.main()