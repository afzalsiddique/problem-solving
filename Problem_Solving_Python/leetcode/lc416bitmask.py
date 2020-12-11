# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C%2B%2B-4-line-solution-using-a-bitset
# https://leetcode.com/problems/partition-equal-subset-sum/discuss/90590/Simple-C++-4-line-solution-using-a-bitset/94973

class Solution(object):

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_val = 0
        bits = 1
        bin_bits = bin(bits)
        for num in nums:
            sum_val += num
            temp = bits << num
            bin_temp = bin(temp)
            bits |= temp
            bin_bits = bin(bits)

        return (not sum_val % 2 == 1) and (bits >> (sum_val // 2)) & 1 == 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.canPartition([6,4,7,5]))