# -*- encoding: utf-8 -*-
'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.total = 0
        path = ""

        self.dfs(root, path)

        return self.total

    def dfs(self, root, path):
        if root == None:
            return

        if root.left == None and root.right == None:
            self.total += int(path + str(root.val))
            return 

        path = path + str(root.val)
        if root.left != None:
            self.dfs(root.left, path)

        if root.right != None:
            self.dfs(root.right, path)
