import unittest
from hello import sayHello

class TestFileName(unittest.TestCase):
  def test_sayHello(self):
    greeting = sayHello()
    self.assertEqual(greeting, "Hello All World")
    
if __name__ == '__main__':
  unittest.main()