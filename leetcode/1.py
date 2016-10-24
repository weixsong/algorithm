'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above updated description carefully.
'''

'''
Solution 1: sort the nums and record the original indices
'''


class Solution(object):
    """
    sort the nums, and record the original indices
    then search from left and right

    O(nlogn)
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums = [(nums[i], i) for i in range(len(nums))]
        nums = sorted(nums, key=lambda x: x[0])

        left, right = 0, len(nums) - 1
        while left < right:
            temp = nums[left][0] + nums[right][0]
            if temp == target:
                return [nums[left][1], nums[right][1]]
            if temp < target:
                left += 1
            else:
                right -= 1


'''
solution 2: by hash table
'''
class Solution(object):
    """
    O(n)
    using hash table to lookup another number in this hash table given another number,
    if another number is in hash table, then we could get number indices.
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        indices = {}
        for i in xrange(len(nums)):
            if nums[i] in indices and nums[i] * 2 == target:
                return [indices[nums[i]], i]

            indices[nums[i]] = i

        for i in xrange(len(nums)):
            n1 = nums[i]
            n2 = target - n1
            if n2 in indices and n1 != n2:
                return [indices[n1], indices[n2]]
