#!/usr/bin/env python

class Power(object):
    '''
    Power contains some static function that could do quick bit operation.
    '''

    @staticmethod
    def isPowerOfTwo(n):
        '''
        :type n: int
        :rtype: bool

        Given an integer, write a function to determine if it is a power of two.

        Idea: bit operation, if n is power of 2, then it bit representation only contains one 1, 
        '''

        if n == 0:
            return False

        return n & (n - 1) == 0
