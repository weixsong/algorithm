'''
Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
'''

class Solution:
    '''
    O(n)
    '''
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if nums == None or len(nums) == 0 or k <=0: return False

        pre = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in pre:
                if i - pre[num] <= k: return True
            pre[num] = i

        return False


if __name__ == '__main__':
    a = [-1, -1]
    so = Solution()

    print so.containsNearbyDuplicate(a, 1)

