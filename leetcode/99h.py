# -*- encoding: utf-8 -*-
'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    Morris inorder traverse
    '''
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        first, second = None, None
        pre = None

        while root != None:
            if root.left != None:
                temp = root.left

                while temp.right != None and temp.right != root:
                    temp = temp.right

                if temp.right != None:
                    if pre != None and pre.val > root.val:
                        if first == None:
                            first = pre

                        second = root

                    pre = root
                    temp.right = None
                    root = root.right

                else:
                    temp.right = root
                    root = root.left

            else:
                if pre != None and pre.val > root.val:
                    if first == None:
                        first = pre
                    second = root
                pre = root
                root = root.right


        if first != None and second != None:
            first.val, second.val = second.val, first.val


