# -*- encoding: utf-8 -*-
'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        left, right = 0, len(nums) - 1
        return self.build_tree(nums, left, right)

    def build_tree(self, nums, left, right):
        if left > right:
            return None

        mid = left + (right - left) / 2
        tree_node = TreeNode(nums[mid])
        tree_node.left = self.build_tree(nums, left, mid - 1)
        tree_node.right = self.build_tree(nums, mid + 1, right)

        return tree_node
