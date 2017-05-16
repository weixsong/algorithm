# -*- encoding: utf-8 -*-

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''

class Solution2:
    '''
    O(n^2logn)
    overtime
    '''
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        l = len(nums)
        res = {}

        for i in range(l - 1):
            for j in range(i + 1, l):
                total = nums[i] + nums[j]
                neg = -total

                # binary search
                k, n = j + 1, l - 1
                while k <= n:
                    mid = k + (n - k) / 2
                    if nums[mid] == neg: res[(nums[i], nums[j], nums[mid])] = 1
                    if nums[mid] > neg: n = mid - 1
                    else: k = mid + 1

        return res.keys()


class Solution:
    '''
    O(n^2)
    '''
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if len(nums) <= 2: return []
        nums.sort()
        if nums[0] > 0: return []
        l = len(nums)
        res = {}

        for idx in range(l):
            if idx > 0 and nums[idx] == nums[idx-1]: continue
            num = nums[idx]
            if num > 0: break

            neg = -num
            if idx + 2 < l and nums[idx + 1] + nums[idx + 2] > neg: break

            s, n = idx + 1, l - 1
            while s < n:
                total = nums[s] + nums[n]
                if total == neg:
                    res[(num, nums[s], nums[n])] = 1
                    s += 1
                    n -= 1
                elif total > neg:
                    n -= 1
                else:
                    s += 1

        return res.keys()
        

if __name__ == '__main__':
    a = [-1, 0, 1, 2, -1, -4]

    so = Solution()
    print so.threeSum(a)

