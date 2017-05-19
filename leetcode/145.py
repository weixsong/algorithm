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

class Solution1(object):
    '''
    recursive
    '''
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []
        self.post_traverse(root, res)

        return res

    def post_traverse(self, root, res):
        if root == None:
            return

        self.post_traverse(root.left, res)
        self.post_traverse(root.right, res)

        res.append(root.val)

class Solution(object):
    '''
    iterative
    '''
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        visited = set()
        res = []
        stack = [root]
        while len(stack) != 0:
            front = stack[len(stack) - 1]
            if front in visited:
                stack.pop()
                res.append(front.val)
                continue

            if front.right != None:
                stack.append(front.right)

            if front.left != None:
                stack.append(front.left)

            visited.add(front)

        return res



