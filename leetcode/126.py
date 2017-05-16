#!/usr/bin/env python
"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """

        import collections
        wordlist.add(endWord)
        level = {beginWord}
        # parent also record the visited node by previous level
        parent = collections.defaultdict(set)

        found = False
        while len(level) > 0:
            next_level = collections.defaultdict(set)
            for word in level:
                if word == endWord:
                    found = True
                    break
                for new_ch in 'abcdefghijklmnopqrstuvwxyz':
                    for i in range(len(word)):
                        new_word = word[:i] + new_ch + word[i + 1:]

                        # check if valid new word
                        if new_word not in wordlist:
                            continue

                        # a new word could has more than one parent, if the new word is not visited and is a valid
                        # word in wordList, then it is next level word and should record it's parent
                        if new_word not in parent:
                            next_level[new_word].add(word)

            level = next_level
            parent.update(next_level)

            if found == True:
                break

        if found == False:
            return []

        res = self.backtrace(beginWord, endWord, parent)
        return res
    
    def backtrace(self, beginWord, endWord, parent):
        """
        backtrace from endWord to beginWord
        """
        res = [[endWord]]

        while res and res[0][0] != beginWord:
            new_res = []
            for row in res:
                for p in parent[row[0]]:
                    new_row = row[:]
                    new_row.insert(0, p)
                    new_res.append(new_row)

            res = new_res

        return res

# reference
class Solution2:
    def findLadders(self, start, end, dic):
        import string
        import collections
        dic.add(end)
        level = {start}
        parents = collections.defaultdict(set)
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in string.ascii_lowercase:
                    for i in range(len(start)):
                        n = node[:i]+char+node[i+1:]
                        if n in dic and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res

if __name__ == '__main__':
    so = Solution()

    res = so.findLadders('hit', 'cog', set(["hot","dot","dog","lot","log"]))
    for row in res:
        print row

    res = so.findLadders('hot', 'dog', set(["hot","dog"]))
    for row in res:
        print row
