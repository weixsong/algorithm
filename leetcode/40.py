# -*- encoding: utf-8 -*-
'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 

'''

class Solution2(object):
    '''
    DFS, recursively
    timeout
    '''
    def combinationSum2(self, candidates, target):
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
            res.add(tuple(comb[:]))
            return

        if sum(comb) > target:
            return

        for j in range(idx, len(candidates)):
            comb.append(candidates[j])
            self.dp(candidates, target, j + 1, res, comb)
            comb.pop()

class Solution(object):
    '''
    DFS, iteratively
    '''
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        stack = [(0, 0, [])]
        result = set()
        while stack:
            total, start, res = stack.pop()
            if total == target:
                result.add(tuple(res))
            for idx in range(start, len(candidates)):
                t = total + candidates[idx]
                if t > target:
                    break
                stack.append((t, idx + 1, res + [candidates[idx]]))

        return list(result)

if __name__ == '__main__':
    so = Solution()

    print so.combinationSum2([10,1,2,7,6,1,5], 8)

