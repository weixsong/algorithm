'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
    	if len(strs) == 0: return ''
    	res = []

    	idx = 0
    	ml = float('inf')
    	for s in strs:
    		if len(s) < ml: ml = len(s)

    	while idx < ml:
    		c = strs[0][idx]
    		for s in strs:
    			if s[idx] != c:
    				return ''.join(res)

    		res.append(c)
    		idx += 1

    	return ''.join(res)

if __name__ == '__main__':
	so = Solution()
	strs = ['abc', 'ab', 'abcde', 'abe']
	print so.longestCommonPrefix(strs)

	strs = []
	print so.longestCommonPrefix(strs)
