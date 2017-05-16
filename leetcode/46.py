# -*- encoding: utf-8 -*-
'''
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = set()
        self.solve(nums, 0, len(nums), res)
        return list(res)

    def solve(self, nums, k, length, res):
        if k == length:
            res.add(tuple(nums[:]))
            return

        for i in range(k, length):
            nums[k], nums[i] = nums[i], nums[k]
            self.solve(nums, k + 1, length, res)
            nums[k], nums[i] = nums[i], nums[k]

class Solution2(object):
    '''
    need to check if a new num is already in the current permutation
    iterative implementation
    '''
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = set([()])
        for dummy_idx in range(len(nums)):
            temp = set()
            for seq in ans:
                seq_set = set(seq)
                for num in nums:
                    if num in seq_set:
                        continue
                    new_seq = list(seq)
                    new_seq.append(num)
                    temp.add(tuple(new_seq))

            ans = temp

        return list(ans)

class Solution(object):
    '''
    reduce duplicate
    '''
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = set()
        self.solve(nums, 0, res)
        return list(res)

    def solve(self, nums, k, res):
        if k == len(nums):
            res.add(tuple(nums[:]))
            return

        processed = set()
        for i in xrange(k, len(nums)):
            if nums[i] in processed:
                continue
            nums[k], nums[i] = nums[i], nums[k]
            processed.add(nums[i])
            self.solve(nums, k + 1, res)
            nums[k], nums[i] = nums[i], nums[k]

class Solution(object):
    '''
    reduce duplicate
    '''
    def permute(self, nums):
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



if __name__ == '__main__':
    so = Solution2()

    print so.permute([1, 2, 3])
