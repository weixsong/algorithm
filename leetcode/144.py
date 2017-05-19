# -*- encoding: utf-8 -*-
'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    recursive
    '''
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []
        self.pre_traverse(root, res)
        return res

    def pre_traverse(self, root, res):
        if root == None:
            return

        res.append(root.val)
        self.pre_traverse(root.left, res)
        self.pre_traverse(root.right, res)

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        stack = [root]
        res = []
        while len(stack) != 0:
            front = stack.pop()
            res.append(front.val)

            if front.right != None:
                stack.append(front.right)
            if front.left != None:
                stack.append(front.left)

        return res
