# -*- encoding: utf-8 -*-
'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        q = [root]
        res = []

        while len(q) != 0:
            temp = []
            level_val = []
            for node in q:
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)

                level_val.append(node.val)

            q = temp
            res.append(level_val)

        res.reverse()
        return res



