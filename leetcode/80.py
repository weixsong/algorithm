# -*- encoding: utf-8 -*-
'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 2:
            return len(nums)

        pre1, pre2 = nums[0], nums[1]
        idx = 2

        for i in range(2, len(nums)):
            if nums[i] == pre1 and nums[i] == pre2:
                continue

            nums[idx] = nums[i]
            pre1 = pre2
            pre2 = nums[idx]
            idx += 1

        return idx

if __name__ == '__main__':
    so = Solution()

    print so.removeDuplicates([1,1,1,2,2,3])
    print so.removeDuplicates([1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,4])
    print so.removeDuplicates([1,1,1,3,3])