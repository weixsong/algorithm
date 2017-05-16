# -*- encoding: utf-8 -*-
'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    correct
    '''
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root == None or p == None or q == None:
            return None

        l1 = []
        self.pre_order_traverse(root, p, l1)

        l2 = []
        self.pre_order_traverse(root, q, l2)

        if len(l1) == 0 or len(l2) == 0:
            return None

        i, j = len(l1) - 1, len(l2) - 1
        pre = len(l1)
        while i >= 0 and j >= 0:
            if l1[i] == l2[j]:
                pre = i
                i -= 1
                j -= 1
            else:
                break

        return l1[pre]

    def pre_order_traverse(self, root, node, res):
        if root == None:
            return False

        if root == node:
            res.append(root)
            return True

        found = self.pre_order_traverse(root.left, node, res)
        if found == True:
            res.append(root)
            return found

        found = self.pre_order_traverse(root.right, node, res)
        if found == True:
            res.append(root)

        return found


class Solution(object):
    '''
    recursive implementation
    '''
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root == None:
            return None

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if p == root or q == root or (left and right):
            return root
        else:
            return left if left else right








