# -*- encoding: utf-8 -*-
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

'''

class Solution2(object):
    '''
    time out
    really bad time complex
    '''
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = set()
        res.add(tuple(nums[:]))
        self.solve(nums, 0, len(nums), res)
        return list(res)

    def solve(self, nums, k, length, res):
        if k >= length:
            res.add(tuple(nums[:]))
            return

        for i in range(k, length):
            if i < length - 1 and nums[i] == nums[i + 1]:
                res.add(tuple(nums[:]))
                continue
            nums[k], nums[i] = nums[i], nums[k]
            self.solve(nums, k + 1, length, res)
            nums[k], nums[i] = nums[i], nums[k]

class Solution1(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = set()
        stack = []
        nums.sort()
        self.solve(nums, res, stack, len(nums))
        return list(res)

    def solve(self, nums, res, stack, k):
        if k == len(stack):
            res.add(tuple(stack[:]))
            return

        for i in range(len(nums)):
            temp = nums[i]
            nums.pop(i)
            stack.append(temp)

            self.solve(nums, res, stack, k)

            stack.pop()
            nums.insert(i, temp)

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = set()
        stack = []
        nums.sort()
        self.solve(nums, res, stack, len(nums))
        return list(res)

    def solve(self, nums, res, stack, k):
        if k == len(stack):
            res.add(tuple(stack[:]))
            return

        i = 0
        while i < len(nums):
            temp = nums[i]
            nums.pop(i)
            stack.append(temp)

            self.solve(nums, res, stack, k)

            stack.pop()
            nums.insert(i, temp)

            # if same num push into stack, it will lead to the same permutation
            # if push the same value to stack, then will lead to same stack as previous
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            i += 1



if __name__ == '__main__':
    so = Solution()

    #nums = [3,3,0,0,2,3,2]
    nums = [1, 1, 2]
    print so.permuteUnique(nums)

    print so.permuteUnique([1,2,3])

    print so.permuteUnique([1,1,1,5])