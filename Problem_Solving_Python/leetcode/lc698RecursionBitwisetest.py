import unittest
from leetcode.lc698RecursionBitwise import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908]
        k = 4
        actual = solution.canPartitionKSubsets(nums, k)
        expected = True
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908]
        k = 4
        actual = solution.canPartitionKSubsets(nums, k)
        expected = True
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
