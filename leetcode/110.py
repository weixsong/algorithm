# -*- encoding: utf-8 -*-
'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        res = self.traverse(root)
        return res[1]

    def traverse(self, root):
        if root == None:
            return 0, True

        lh, res = self.traverse(root.left)
        if res == False:
            return lh, False

        rh, res = self.traverse(root.right)
        if res == False:
            return rh, False

        if abs(lh - rh) > 1:
            return max(lh, rh), False

        return max(lh, rh) + 1, True

