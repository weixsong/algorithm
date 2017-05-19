# -*- encoding: utf-8 -*-
'''
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        tree_max, path_max = self.post_traverse(root)
        return tree_max

    def post_traverse(self, node):
        if node.left == None and node.right == None:
            return node.val, node.val

        if node.left != None:
            tm_left, pm_left = self.post_traverse(node.left)

        if node.right != None:
            tm_right, pm_right = self.post_traverse(node.right)

        if node.left != None and node.right != None:
            tree_max = max(tm_left, tm_right, node.val, pm_left + node.val, pm_right + node.val, pm_left + pm_right + node.val)
            path_max = max(pm_left + node.val, pm_right + node.val, node.val)
            return tree_max, path_max

        elif node.left != None and node.right == None:
            tree_max = max(tm_left, pm_left + node.val, node.val)
            path_max = max(pm_left + node.val, node.val)
            return tree_max, path_max

        else:
            tree_max = max(tm_right, pm_right + node.val, node.val)
            path_max = max(pm_right + node.val, node.val)
            return tree_max, path_max




if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    so = Solution()
    print so.maxPathSum(root)

    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(-1)
    root.right.left = TreeNode(-2)

    print so.maxPathSum(root)

    root = TreeNode(-2)
    root.right = TreeNode(-3)

    print so.maxPathSum(root)


    root = TreeNode(5)
    root.right = TreeNode(-2)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(-1)
    root.right.right.right = TreeNode(4)

    print so.maxPathSum(root)
