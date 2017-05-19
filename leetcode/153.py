# -*- encoding: utf-8 -*-
'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''

class Solution1(object):
    '''
    binary search variants
    '''
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left, right = 0, len(nums) - 1

        if nums[left] <= nums[right]:
            return nums[left]

        while nums[left] > nums[right]:
            if right - left == 1:
                break
            mid = left + (right - left) / 2

            if nums[mid] >= nums[left]:
                left = mid
            elif nums[mid] <= nums[right]:
                right = mid

        return nums[right]

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
            if nums[left] <= nums[right]:
                break

            mid = left + (right - left) / 2
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

if __name__ == '__main__':
    so = Solution()

    print so.findMin([4, 5, 6, 7, 0, 1, 2])
    print so.findMin([1, 2])
    print so.findMin([3,1,2])



