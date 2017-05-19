# -*- encoding: utf-8 -*-
'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return [[]]

        left, right = 1, n

        return self.build(left, right)

    def build(self, left, right):
        if left > right:
            return []

        sub_trees = []
        for i in range(left, right + 1):
            left_sub_trees = self.build(left, i - 1)
            right_sub_trees = self.build(i + 1, right)

            if len(left_sub_trees) == 0 and len(right_sub_trees) == 0:
                # no left sub tree and no right sub tree
                tree_node = TreeNode(i)
                sub_trees.append(tree_node)

            elif len(left_sub_trees) != 0 and len(right_sub_trees) != 0:
                for node_l in left_sub_trees:
                    for node_r in right_sub_trees:
                        tree_node = TreeNode(i)
                        tree_node.left = node_l
                        tree_node.right = node_r

                        sub_trees.append(tree_node)

            elif len(left_sub_trees) != 0 and len(right_sub_trees) == 0:
                for node in left_sub_trees:
                    tree_node = TreeNode(i)
                    tree_node.left = node

                    sub_trees.append(tree_node)

            elif len(left_sub_trees) == 0 and len(right_sub_trees) != 0:
                for node in right_sub_trees:
                    tree_node = TreeNode(i)
                    tree_node.right = node

                    sub_trees.append(tree_node)

        return sub_trees

            



