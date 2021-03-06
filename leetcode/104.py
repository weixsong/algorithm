# -*- encoding: utf-8 -*-
'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return self.traverse(root)

    def traverse(self, root):
        if root == None:
            return 0

        l = self.traverse(root.left)
        r = self.traverse(root.right)

        return max(l, r) + 1
