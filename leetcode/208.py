# -*- encoding: utf-8 -*-
'''
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

'''

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.children = {}
        

class Trie(object):

    def __init__(self):
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}

            node = node[c]

        node['wesong'] = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        node = self.root
        for c in word:
            if c not in node:
                return False

            node = node[c]

        return 'wesong' in node
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        node = self.root
        for c in prefix:
            if c not in node:
                return False

            node = node[c]

        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")