# -*- encoding: utf-8 -*-
'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        nums = []
        self.inorder(root, nums)

        if len(nums) < 2:
            return True

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False

        return True


    def inorder(self, node, nums):
        if node == None:
            return

        self.inorder(node.left, nums)
        nums.append(node.val)
        self.inorder(node.right, nums)


