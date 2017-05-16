# -*- encoding: utf-8 -*-
'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        res = []
        self.in_order_traverse(root, res)

        return res

    def in_order_traverse(self, root, res):
        if root == None:
            return

        self.in_order_traverse(root.left, res)
        res.append(root.val)
        self.in_order_traverse(root.right, res)

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if root == None:
            return []
        
        stack = [root]
        res = []
        visited = set()

        while len(stack) != 0:
            front = stack.pop()
            if front.left != None and front.left not in visited:
                stack.append(front)
                stack.append(front.left)
                continue

            visited.add(front)
            res.append(front.val)
            if front.right != None:
                stack.append(front.right)

        return res




