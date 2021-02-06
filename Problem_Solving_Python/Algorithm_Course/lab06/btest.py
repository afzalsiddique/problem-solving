import unittest
from Algorithm_Course.lab06.b import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        src,dst=5,6
        cap=[
            [0,0,0,0,0,0,0],
            [0,0,5,10,13,0,0],
            [0,0,0,5,7,0,0],
            [0,0,0,0,20,0,0],
            [0,0,0,0,0,0,100000],
            [0,100000,100000,100000,0,0,0],
            [0,0,0,0,0,0]
        ]
        actual = ford(src,dst,4,cap)
        expected = 37
        self.assertEqual(expected, actual)