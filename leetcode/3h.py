'''
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''

class Solution3:
    '''
    O(n^2)
    overtime
    '''
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        longest_len = 0
        start, end = -1, -1
        for i in range(len(s) - 1):
            cset = set()
            repeat = False
            for j in range(i, len(s)):
                if s[j] not in cset:
                    cset.add(s[j])
                else:
                    # find repeat
                    repeat = True
                    break
            
            if repeat == False:
                clen = j - i + 1
                if clen > longest_len:
                    longest_len = clen
                    start = i
                    end = j
            else:
                clen = j - i
                if clen > longest_len:
                    longest_len = clen
                    start = i
                    end = j - 1

        return s[start : end + 1]

class Solution2:
    '''
    O(n)
    '''
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        num_char = len(set(s))
        longest = 0
        for i in range(len(s)):
            if i + longest >= len(s): break
            max_len = 0
            begin = i
            idx = i
            search_end = begin + num_char - 1

            while idx < len(s):
                left = idx
                cset = set()
                while idx <= len(s) - 1 and s[idx] not in cset:
                    cset.add(s[idx])
                    idx += 1
                clen = idx - left
                if clen > max_len:
                    max_len = clen
                    begin = left

            if max_len > longest:
                longest = max_len

        return longest

class Solution:
    '''
    O(n)
    '''
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        pre = {}
        max_len, cur_len = 0, 0

        for i in range(len(s)):
            c = s[i]
            if c not in pre or i - cur_len > pre[c]:
                cur_len += 1
            else:
                if cur_len > max_len: max_len = cur_len
                cur_len = i - pre[c]

            pre[c] = i

        if cur_len > max_len: max_len = cur_len
        return max_len

if __name__ == '__main__':

    so = Solution()


    s = "dvdf"
    print so.lengthOfLongestSubstring(s)

    s = "abba"
    print so.lengthOfLongestSubstring(s)

