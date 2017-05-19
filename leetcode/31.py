# -*- encoding: utf-8 -*-
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        n = len(nums)
        i, j = n - 2, n - 1
        while i >= 0 and j >= 0:
            if nums[i] >= nums[j]:
                i -= 1
                j -= 1
            else:
                break

        if i < 0:
            nums.sort()
            return

        min_v = nums[j]
        idj = j
        while j < n:
            if nums[j] < min_v and nums[j] > nums[i]:
                min_v = nums[j]
                idj = j

            j += 1

        j = idj
        nums[i], nums[j] = nums[j], nums[i]

        # sort from j
        self.sort(nums, i + 1, n - 1)

    def sort(self, nums, left, right):
        if left < right:
            pivot = self.partition(nums, left, right)
            self.sort(nums, left, pivot - 1)
            self.sort(nums, pivot + 1, right)

    def partition(self, nums, left, right):
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1

            nums[left], nums[right] = nums[right], nums[left]

            while left < right and nums[left] <= pivot:
                left += 1

            nums[left], nums[right] = nums[right], nums[left]

        return left

if __name__ == '__main__':
    so = Solution()

    nums = [2,3,1]
    print so.nextPermutation(nums)
    print nums

