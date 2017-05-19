# -*- encoding: utf-8 -*-
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root == None:
            return []

        q = [root]
        res = []
        depth = 0

        while len(q) != 0:
            depth += 1

            temp = []
            values = []

            for node in q:
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)

            if depth % 2 == 0:
                q.reverse()

            for node in q:
                values.append(node.val)

            q = temp
            res.append(values)

        return res


