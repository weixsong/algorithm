# -*- encoding: utf-8 -*-
'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        res = []
        q = [root]

        while len(q) != 0:
            res.append(q[len(q) - 1].val)

            temp = []
            for item in q:
                if item.left != None:
                    temp.append(item.left)
                if item.right != None:
                    temp.append(item.right)

            q = temp

        return res
