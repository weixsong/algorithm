# -*- encoding: utf-8 -*-
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

class Solution(object):
    def levelOrder(self, root):
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

        return res

