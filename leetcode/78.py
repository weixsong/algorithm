# -*- encoding: utf-8 -*-
'''
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = [[]]

        for num in nums:
            temp = res[:]
            for subset in temp:
                new_set = subset[:]
                new_set.append(num)
                new_set.sort()
                res.append(new_set)

        return res

if __name__ == '__main__':
    so = Solution()

    print so.subsets([1,2,3])
