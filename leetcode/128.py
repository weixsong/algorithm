#!/usr/bin/env python
"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums == None or len(nums) < 1:
            return 0

        nums.sort()
        cur, best = 1, 1

        print nums

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                cur += 1
                best = max(best, cur)
            else:
                cur = 1

        return best

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time: O(nlogn)
        """
        
        if nums == None or len(nums) < 1:
            return 0

        nums = list(set(nums))
        nums.sort()
        cur, best = 1, 1

        print nums

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur += 1
                best = max(best, cur)
            else:
                cur = 1

        return best

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time: O(n)
        """
        
        if nums == None or len(nums) == 0:
            return 0

        collection = set(nums)
        best = 0

        for num in nums:
            if num in collection:
                val = num
                step = 1

                collection.remove(val)

                # remove left
                while val - 1 in collection:
                    collection.remove(val - 1)
                    step += 1
                    val -= 1

                # remove right
                val = num
                while val + 1 in collection:
                    collection.remove(val + 1)
                    step += 1
                    val += 1

                best = max(best, step)

        return best


if __name__ == '__main__':
    so = Solution()

    print so.longestConsecutive([1,2,0,1])
