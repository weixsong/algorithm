# -*- encoding: utf-8 -*-
'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''

class Solution1(object):
    '''
    permutation directly will lead to timeout
    '''
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        cand = [i for i in range(1, n + 1)]
        fact = self.factorail(n)
        res = []
        while n > 0:
            fact /= n

            target = cand[0]
            for num in cand:
                childs = fact
                target = num
                if childs < k:
                    k -= fact
                else:
                    break

            cand.remove(target)
            res.append(str(target))
            n -= 1

        return ''.join(res)

    def factorail(self, k):
        res = 1
        while k > 0:
            res *= k
            k -= 1

        return res

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        numbers = range(1, n + 1)
        permutation = []
        k -= 1

        fact = 1
        f = n
        while f > 0:
            fact *= f
            f -= 1

        while n > 0:
            fact /= n
            n -= 1
            # get the index of current digit
            index, k = divmod(k, fact)
            permutation.append(str(numbers[index]))
            # remove handled number
            numbers.remove(numbers[index])

        return ''.join(permutation)

if __name__ == '__main__':
    so = Solution()
    print so.getPermutation(3, 1)
    print so.getPermutation(3, 2)
    print so.getPermutation(3, 3)
    print so.getPermutation(3, 4)
    print so.getPermutation(3, 5)
    print so.getPermutation(3, 6)

