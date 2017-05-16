# -*- encoding: utf-8 -*-
'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

class Solution(object):
    '''
    Random selection: O(n)
    '''

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        i, j = 0, len(nums) - 1
        r = self.partition(nums, i, j)
        while r != k - 1:
            if r > k:
                j = r - 1
            if r < k:
                i = r + 1

            r = self.partition(nums, i, j)

        return nums[r]


    def partition(self, nums, i, j):
        pivot = nums[i]

        while i < j:
            while i < j and nums[j] <= pivot:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

            while i < j and nums[i] >= pivot:
                i += 1

            nums[i], nums[j] = nums[j], nums[i]

        return i

if __name__ == '__main__':
    so = Solution()

    num = [3,2,1,5,6,4]
    k = 2

    print so.findKthLargest(num, k)

    

