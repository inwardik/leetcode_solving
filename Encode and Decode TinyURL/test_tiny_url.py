import unittest
from tiny_url import Codec

class TestSolution(unittest.TestCase):
    def test_codec(self):
        codec = Codec()
        self.assertEqual(codec.encode("http://www.fullondesign.co.uk/"),'https://tinyurl.com/d4px9f')
        self.assertEqual(codec.decode("https://tinyurl.com/d4px9f"), "http://www.fullondesign.co.uk/")




if __name__ == '__main__':
    unittest.main()