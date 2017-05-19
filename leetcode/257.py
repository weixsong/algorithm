# -*- encoding: utf-8 -*-
'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []

        res = []
        path = []

        self.traverse(root, res, path)

        r = []
        for path in res:
            r.append('->'.join([str(i) for i in path]))
        return r

    def traverse(self, root, res, path):
        if root.left == None and root.right == None:
            temp = path[:]
            temp.append(root.val)
            res.append(temp)
            return

        path.append(root.val)
        if root.left != None:
            self.traverse(root.left, res, path)

        if root.right != None:
            self.traverse(root.right, res, path)

        path.pop()

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)

    so = Solution()

    print so.binaryTreePaths(root)