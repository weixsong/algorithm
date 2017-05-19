# -*- encoding: utf-8 -*-
'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        i, j = 0, len(nums) - 1
        count = 0
        while i <= j:
            if nums[i] == val:
                count += 1
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1

        for k in range(count):
            nums.pop()

        return len(nums)

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        int j = nums.size() - 1;
        int count = 0;
        
        while (i <= j)
        {
            if (nums[i] == val)
            {
                count++;
                nums[i] = nums[j];
                j--;
            }
            else
            {
                i += 1;
            }
        }
        
        
        for (int k = count; k > 0; k--)
        {
            nums.pop_back();
        }
        
        return nums.size();
    }
};

if __name__ == '__main__':
    so = Solution()

    nums = [1]

    so.removeElement(nums, 1)
    print nums

