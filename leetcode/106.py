# -*- encoding: utf-8 -*-
'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        self.pointer = len(postorder) - 1
        left, right = 0, len(inorder) - 1

        return self.build_tree(inorder, postorder, left, right)

    def build_tree(self, inorder, postorder, left, right):
        if left > right:
            return None

        target = postorder[self.pointer]
        tree_node = TreeNode(target)
        self.pointer -= 1

        pos = self.find_target(inorder, left, right, target)

        if pos < right:
            # contain right child
            tree_node.right = self.build_tree(inorder, postorder, pos + 1, right)
        if pos > left:
            # contain left child
            tree_node.left = self.build_tree(inorder, postorder, left, pos - 1)

        return tree_node

    def find_target(self, inorder, left, right, target):
        for idx in range(left, right + 1):
            if inorder[idx] == target:
                return idx


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.pointer = len(postorder) - 1
        left, right = 0, len(inorder) - 1
        return self.build(inorder, postorder, left, right)

    def build(self, inorder, postorder, left, right):
        if left > right:
            return None

        target = postorder[self.pointer]
        tree_node = TreeNode(target)
        self.pointer -= 1

        pos = inorder.index(target)

        if pos < right:
            # contain right child
            tree_node.right = self.build(inorder, postorder, pos + 1, right)
        if pos > left:
            # contain left child
            tree_node.left = self.build(inorder, postorder, left, pos - 1)

        return tree_node


if __name__ == '__main__':
    so = Solution()

    inorder = [1, 2, 3]
    postorder = [2, 1, 3]

    tree = so.buildTree(inorder, postorder)
    print tree.val

    inorder = [2, 1]
    postorder = [2, 1]

    tree = so.buildTree(inorder, postorder)
    print tree.val
