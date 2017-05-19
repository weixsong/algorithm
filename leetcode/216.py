# -*- encoding: utf-8 -*-
'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution1(object):
    '''
    DFS, recursively
    '''
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        res = []
        comb = []
        self.dfs(1, res, comb, k, n)

        return res

    def dfs(self, idx, res, comb, k, n):
        if sum(comb) == n and len(comb) == k:
            res.append(comb[:])
            return

        if sum(comb) > n:
            return

        if len(comb) > k:
            return

        for j in range(idx, 10):
            comb.append(j)
            self.dfs(j + 1, res, comb, k, n)
            comb.pop()

class Solution(object):
    '''
    DFS, iteratively
    '''
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        stack = [(1, [])]
        result = []
        while stack:
            start, nums = stack.pop()
            if sum(nums) == n and len(nums) == k:
                result.append(nums[:])

            if sum(nums) > n or len(nums) > k:
                continue

            for idx in range(start, 10):
                new_nums = nums[:]
                new_nums.append(idx)
                stack.append((idx + 1, new_nums))

        return result

if __name__ == '__main__':
    so = Solution()

    print so.combinationSum3(3, 9)
