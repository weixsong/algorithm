# -*- encoding: utf-8 -*-
'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        if root == None:
            return

        self.post_order_traverse(root)

    def post_order_traverse(self, root):
        if root.right != None:
            self.post_order_traverse(root.right)

        if root.left != None:
            self.post_order_traverse(root.left)

        if root.left != None and root.right != None:
            node = root.left
            while node.right != None:
                node = node.right
                node.left = None
            node.right = root.right
            root.right = root.left
            root.left = None

        if root.left != None and root.right == None:
            root.right = root.left
            root.left = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        if root == None:
            return

        self.post_order_traverse(root)

    def post_order_traverse(self, root):
        if root.right == None and root.left == None:
            return root

        r_last, l_last = None, None
        if root.right != None:
            r_last = self.post_order_traverse(root.right)

        if root.left != None:
            l_last = self.post_order_traverse(root.left)

        if l_last != None and r_last != None:
            l_last.right = root.right
            root.right = root.left
            root.left = None
            return r_last

        elif l_last != None and r_last == None:
            root.right = root.left
            root.left = None
            return l_last
            
        else:
            return r_last





