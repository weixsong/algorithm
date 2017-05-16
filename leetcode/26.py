# -*- encoding: utf-8 -*-
'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = []
        pre = None
        idx = -1

        for i in range(len(nums)):
            if nums[i] == pre:
                continue

            idx += 1
            nums[idx] = nums[i]
            pre = nums[i]

        idx += 1
        k = idx
        while idx < len(nums):
            nums.pop()
            idx += 1

        return k

if __name__ == '__main__':
    so = Solution()

    nums = [1,1,2]
    so.removeDuplicates(nums)

    print nums

