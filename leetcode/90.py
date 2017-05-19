# -*- encoding: utf-8 -*-
'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()

        res = set([()])

        i = 0
        while i < len(nums):
            temp = set()

            num = nums[i]
            for sub in res:
                new_sub = list(sub)
                new_sub.append(num)
                temp.add(sub)
                temp.add(tuple(new_sub))

            res = temp
            i += 1

        return list(res)

if __name__ == '__main__':
    so = Solution()
    print so.subsetsWithDup([1, 2, 2])

