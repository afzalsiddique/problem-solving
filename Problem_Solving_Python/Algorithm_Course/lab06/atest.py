import unittest
from Algorithm_Course.lab06.a import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        src,dst=1,4
        cap=[
            [0,0,0,0,0],
            [0,0,20,10,0],
            [0,20,0,5,10],
            [0,10,5,0,20],
            [0,0,10,20,0]
        ]
        actual = ford(src,dst,4,cap)
        expected = 25
        self.assertEqual(expected, actual)