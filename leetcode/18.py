# -*- encoding: utf-8 -*-
'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''

class Solution1(object):
    '''
    O(n^3)
    '''
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) <= 3: return []
        nums.sort()

        res = set()
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i + 1, len(nums)):
                b = nums[j]

                x = target - (a + b)
                if j + 2 < len(nums) and nums[j + 1] + nums[j + 2] > x: continue

                m, n = j + 1, len(nums) - 1
                while m < n:
                    total = nums[m] + nums[n]
                    if total == x:
                        res.add((nums[i], nums[j], nums[m], nums[n]))
                        m += 1
                        n -= 1
                    elif total < x:
                        m += 1
                    else:
                        n -= 1

        return list(res)

class Solution(object):
    '''
    O(n^2logn)
    '''
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import bisect
        if len(nums) <= 3: return []
        nums.sort()

        self.dict = {}
        for i in range(2, len(nums)):
            for j in range(i + 1, len(nums)):
                add = nums[i] + nums[j]
                if add not in self.dict:
                    self.dict[add] = []
                self.dict[add].append((i, j))

        res = set()
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i + 1, len(nums)):
                b = nums[j]

                x = target - (a + b)
                if x not in self.dict:
                    continue
                
                pairs = sorted(self.dict[x], key=lambda item: item[0])
                keys = [r[0] for r in pairs]
                k = bisect.bisect_right(keys, j)
                for idx in range(k, len(pairs)):
                    res.add((nums[i], nums[j], nums[pairs[idx][0]], nums[pairs[idx][1]]))

        return list(res)


if __name__ == '__main__':
    so = Solution()

    s = [1, 0, -1, 0, -2, 2]
    target = 0
    

    print so.fourSum(s, target)

