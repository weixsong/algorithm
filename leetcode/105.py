# -*- encoding: utf-8 -*-
'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        self.pointer = 0
        left, right = 0, len(inorder) - 1
        return self.build(preorder, inorder, left, right)

    def build(self, preorder, inorder, left, right):
        if left > right:
            return None

        target = preorder[self.pointer]
        tree_node = TreeNode(target)
        self.pointer += 1

        pos = inorder.index(target)

        if pos > left:
            # contain left child
            tree_node.left = self.build(preorder, inorder, left, pos - 1)

        if pos < right:
            # contain right child
            tree_node.right = self.build(preorder, inorder, pos + 1, right)

        return tree_node

if __name__ == '__main__':
    so = Solution()

    preorder = [1, 2, 3]
    inorder = [2, 1, 3]

    tree = so.buildTree(preorder, inorder)
    print tree.val