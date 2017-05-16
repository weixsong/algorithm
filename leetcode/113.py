# -*- encoding: utf-8 -*-
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    timeout
    '''
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        path = []
        path_sum = 0
        res = []

        if root == None:
            return res

        self.traverse(root, sum, path, path_sum, res)
        return res

    def traverse(self, node, sum, path, path_sum, res):
        if node.left == None and node.right == None:
            if path_sum + node.val == sum:
                temp = path[:]
                temp.append(node.val)
                res.append(temp)
                
            return

        path.append(node.val)
        if node.left != None:
            self.traverse(node.left, sum, path, path_sum + node.val, res)

        if node.right != None:
            self.traverse(node.right, sum, path, path_sum + node.val, res)

        path.pop()


