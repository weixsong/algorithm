'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        if len(nums) <= 2: return []

        nums.sort()
        l = len(nums)
        diff = float('inf')
        res = float('inf')
        for idx in range(l - 2):
            num1 = nums[idx]
            if idx > 0 and num1 == nums[idx - 1]: continue
            i, j = idx + 1, l - 1
            while i < j:
                total = nums[i] + nums[j]
                c_sum = num1 + total
                c_diff = abs(c_sum - target)
                if c_sum == target:
                    return target
                elif c_diff < diff:
                    diff = c_diff
                    res = c_sum

                if c_sum > target:
                    j -= 1
                else: i += 1

        return res

if __name__ == '__main__':
    so = Solution()
    s = [-1, 2, 1, -4]

    print so.threeSumClosest(s, 1)
