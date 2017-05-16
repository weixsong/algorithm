# -*- encoding: utf-8 -*-
'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
        	return 0

        return self.min_depth(root)

    def min_depth(self, root):
    	# base case
    	if root.left == None and root.right == None:
    		return 1

    	if root.left != None and root.right != None:
    		return min(self.min_depth(root.left), self.min_depth(root.right)) + 1

    	if root.left != None and root.right == None:
    		return self.min_depth(root.left) + 1

    	if root.right != None and root.left == None:
    		return self.min_depth(root.right) + 1


