# -*- encoding: utf-8 -*-
'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''

class Solution2(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        vis = {}
        for word in words:
            vis[word] = vis.get(word, 0) + 1
        
        word_len = len(words[0])
        word_num = len(words)
        substr_len = word_len * word_num

        str_len = len(s)

        i = 0
        res = []

        while i <= str_len - substr_len:
            begin = i
            end = i + substr_len
            idx = i

            found = {}
            while idx < end:
                cand_word = s[idx: idx + word_len]

                if cand_word not in vis:
                    break

                found[cand_word] = found.get(cand_word, 0) + 1
                if found[cand_word] > vis[cand_word]:
                    break

                idx += word_len

            if idx == end:
                res.append(begin)

            i += 1

        return res

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        res = []
        n = len(s)

        word_num = len(words)
        if n <= 0 or word_num <= 0:
            return res

        word_len = len(words[0])

        hist = {}
        for word in words:
            hist[word] = hist.get(word, 0) + 1

        # traverse all possible word combination
        for idx in xrange(word_len):
            left = idx
            count = 0

            table = {}
            j = idx
            while j <= n - word_len:
                sub_str = s[j: j + word_len]
                if sub_str in hist:
                    # a possible word
                    table[sub_str] = table.get(sub_str, 0) + 1
                    if table[sub_str] <= hist[sub_str]:
                        count += 1
                    else:
                        # a more word, move the window correspondingly
                        # until current substr not a more word
                        while table[sub_str] > hist[sub_str]:
                            head_word = s[left: left + word_len]
                            table[head_word] -= 1
                            if table[head_word] < hist[head_word]:
                                count -= 1
                            left += word_len

                    if count == word_num:
                        res.append(left)
                        head_word = s[left: left + word_len]
                        table[head_word] -= 1
                        count -= 1
                        left += word_len

                else:
                    # not valid word
                    table = {}
                    count = 0
                    left = j + word_len

                j += word_len

        return res
        


if __name__ == '__main__':
    so = Solution()

    print so.findSubstring('barfoothefoobarman', ["foo", "bar"])
    print so.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])




