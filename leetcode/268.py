# -*- encoding: utf-8 -*-
'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

class Solution1(object):
    '''
    O(n)
    '''
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = set()

        for num in nums:
            s.add(num)

        for i in range(n + 1):
            if i not in s:
                return i

class Solution(object):
    '''
    O(n)
    using bit xor operation
    '''
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0

        for i in xrange(n + 1):
            total ^= i

        for num in nums:
            total ^= num

        return total

if __name__ == '__main__':
    so = Solution()

    print so.missingNumber([0])
    print so.missingNumber([0, 1, 3])