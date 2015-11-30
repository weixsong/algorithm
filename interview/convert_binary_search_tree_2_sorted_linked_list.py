#!/usr/bin/env python
"""
Given a binary search tree, change it to sorted double linked list by only one pass.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    Inorder traverse.
    """

    def convert(self, tree):
        """
        :type tree: TreeNode
        :rtype: TreeNode

        Idea: by inorder traverse, we could traverse the tree by sorted order, then think it as inorder traverse.
        when visit left sub tree (if exist left tree), we will pass in a node named pre,
        then return from left tree, make pre.next = current_node, current_node.pre = pre
        then visit right sub tree (if exist right sub tree), if no right sub tree, return current_node as the last pre node, 
                                                             else return the node returned from right sub tree.

        Time: O(n)
        Space: O(1)
        """

        head = TreeNode(0)
        self.inorder(tree, head)
        return head.right


    def inorder(self, node, pre):
        if node.left:
            pre = self.inorder(node.left, pre)

        pre.right = node
        node.left = pre

        if node.right:
            return self.inorder(node.right, node)
        else:
            return node

class Traverse(object):
    @staticmethod
    def inorder(node):
        if node != None:
            Traverse.inorder(node.left)
            print node.val
            Traverse.inorder(node.right)

if __name__ == '__main__':
    t = TreeNode(4)

    print 'test #1'
    t.left = TreeNode(2)
    t.right = TreeNode(6)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    t.right.left = TreeNode(5)
    t.right.right = TreeNode(7)

    convertor = Solution()
    res = convertor.convert(t)

    while res != None:
        print res.val,
        res = res.right
    print ''

    print 'test #2'
    t = TreeNode(8)
    t.left = TreeNode(4)
    t.right = TreeNode(11)
    t.left.left = TreeNode(3)
    t.left.left.left = TreeNode(2)
    t.left.left.left.left = TreeNode(1)
    t.left.right = TreeNode(6)
    t.left.right.left = TreeNode(5)
    t.left.right.right = TreeNode(7)
    t.right.left = TreeNode(10)
    t.right.left.left = TreeNode(9)
    t.right.right = TreeNode(13)
    t.right.right.left = TreeNode(12)

    res = convertor.convert(t)

    while res != None:
        print res.val,
        res = res.right

    print ''

    print 'test #3'
    t = TreeNode(5)
    t.left = TreeNode(4)
    t.left.left = TreeNode(3)
    t.left.left.left = TreeNode(2)
    t.left.left.left.left = TreeNode(1)
    t.right = TreeNode(6)


    res = convertor.convert(t)

    while res != None:
        print res.val,
        res = res.right
