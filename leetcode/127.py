#!/usr/bin/env python
"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int

        timeout

        think it as a graph search, BFS
        a word is connected to another word that their distance is 1
        """

        wordList.add(endWord)
        to_visit = [beginWord]

        dist = 1
        while len(to_visit):
            new_to_visit = []
            for word in to_visit:
                if word == endWord:
                    return dist

                new_to_visit += self.getAllWords(word, wordList)

            to_visit = new_to_visit
            dist += 1

        return 0

    def getAllWords(self, word, wordList):
        res = []
        for i in range(len(word)):
            ch = word[i]
            for new_ch in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + new_ch + word[i + 1:]

                if new_word not in wordList:
                    continue

                res.append(new_word)

        return res

if __name__ == '__main__':
    so = Solution()

    print so.ladderLength('hit', 'cog', set(["hot","dot","dog","lot","log"]))

    a = "qa"
    b = "sq"
    l = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    print so.ladderLength(a, b, set(l))
