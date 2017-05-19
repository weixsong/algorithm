# -*- encoding: utf-8 -*-
'''
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
'''

class Solution1(object):
    '''
    O(n)
    '''
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        n = len(citations)
        if n == 0:
            return 0

        for i in xrange(0, len(citations)):
            h = n - i
            if citations[i] >= h:
                return h
                
        return 0

class Solution(object):
    '''
    O(logn)
    '''
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left, right = 0, n - 1

        res = 0
        while left <= right:
            mid = left + (right - left) / 2
            h = n - mid
            if h > citations[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return n - left

if __name__ == '__main__':
    so = Solution()

    print so.hIndex([1])
    print so.hIndex([0, 1, 3, 5, 6])
    print so.hIndex([0, 1])
    print so.hIndex([100])