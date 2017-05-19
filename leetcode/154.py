# -*- encoding: utf-8 -*-
'''
Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

'''

class Solution(object):
    '''
    binary search
    '''
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) / 2
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                # linear search only
                return self.search(nums, left, right)
            elif nums[left] < nums[right]:
                break

            if nums[mid] >= nums[left]:
                # 1st half
                left = mid + 1
            elif nums[mid] <= nums[right]:
                # 2nd half
                if mid - 1 >= left and nums[mid - 1] <= nums[mid]:
                    right = mid - 1
                else:
                    return nums[mid]


        return nums[left]

    def search(self, nums, left, right):
        v = None
        for i in xrange(left, right + 1):
            if v == None or nums[i] < v:
                v = nums[i]

        return v

if __name__ == '__main__':
    so = Solution()

    print so.findMin([4, 5, 6, 7, 0, 1, 2])
    print so.findMin([1, 2])
    print so.findMin([3,1,2])
    print so.findMin([1, 1, 1, 0, 1, 1,1])


