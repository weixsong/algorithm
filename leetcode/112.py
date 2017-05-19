# -*- encoding: utf-8 -*-
'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if root == None:
            return False
        
        path = 0
        return self.traverse(root, sum, 0)

    def traverse(self, node, sum, path):
        if node.left == None and node.right == None:
            # leaf node
            if path + node.val == sum:
                return True
            return False

        if node.left != None:
            res = self.traverse(node.left, sum, path + node.val)
            if res == True:
                return True

        if node.right != None:
            return self.traverse(node.right, sum, path + node.val)

        return False


