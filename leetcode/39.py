# -*- encoding: utf-8 -*-
'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
'''

class Solution1(object):
    '''
    accepted, but not very good.
    Using DFS by recuresively
    '''
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = set()
        comb = []
        candidates.sort()
        self.dp(candidates, target, 0, res, comb)

        return list(res)

    def dp(self, candidates, target, idx, res, comb):
        if sum(comb) == target:
            res.add(tuple(sorted(comb[:])))
            return

        if sum(comb) > target:
            return

        for j in range(idx, len(candidates)):
            comb.append(candidates[j])
            self.dp(candidates, target, j, res, comb)
            comb.pop()

class Solution:
    '''
    DFS by iteratively
    '''
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        stack = [(0, 0, [])]
        result = []
        while stack:
            total, start, res = stack.pop()
            if total == target:
                result.append(res)
            for idx in range(start, len(candidates)):
                t = total + candidates[idx]
                if t > target:
                    break
                stack.append((t, idx, res + [candidates[idx]]))
        return result

if __name__ == '__main__':
    so = Solution()

    print so.combinationSum([2,3,6,7], 7)



