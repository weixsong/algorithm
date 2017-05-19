# -*- encoding: utf-8 -*-
'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.

'''

class Solution2(object):
    '''
    timeout
    '''
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        group = {}
        for word in strs:
            count = {}
            for c in word:
                if c not in count:
                    count[c] = 0
                count[c] += 1

            group[word] = count

        res = []
        while len(strs) != 0:
            l = []
            stat = group[strs[0]]
            for word in strs:
                if group[word] == stat:
                    l.append(word)
                    
            for key in l:
                strs.remove(key)
            l.sort()
            res.append(l)

        return res

class Solution1(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        stat = {}
        for word in strs:
            count = {}
            for c in word:
                if c not in count:
                    count[c] = 0
                count[c] += 1

            stat[word] = count

        group = {}
        for word in strs:
            h = self.get_hash(stat[word])
            if h not in group:
                group[h] = []

            group[h].append(word)

        res = []
        for key in group:
            l = group[key]
            l.sort()
            res.append(l)

        return res

    def get_hash(self, t):
        h = set()
        for key, val in t.iteritems():
            h.add(str(key) + str(val))
        
        l = list(h)
        l.sort()
        return tuple(l)

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dic = {}
        for s in strs:
            hv = tuple(sorted(s))
            if hv not in dic:
                dic[hv] = []

            dic[hv].append(s)

        return [sorted(item) for item in dic.values()]


if __name__ == '__main__':
    so = Solution()

    print so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

    print so.groupAnagrams(["cab","pug","pei","nay","ron","rae","ems","ida","mes"])


