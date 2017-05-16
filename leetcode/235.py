# -*- encoding: utf-8 -*-

'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
    \     /  \
     1    3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    O(n)
    '''
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root == None: return None

        plist, qlist = [], []
        self.searchNode(root, p, plist)
        self.searchNode(root, q, qlist)

        parent = None
        while len(plist) > 0 and len(qlist) > 0:
            a, b = plist.pop(), qlist.pop()
            if a.val == b.val:
                parent = a
            else:
                break

        return parent

    def searchNode(self, root, node, plist):
        '''
        recursive search
        '''
        if root == None: return False

        if root.val == node.val:
            plist.append(root)
            return True
        else:
            find = False
            if root.left: find = self.searchNode(root.left, node, plist)
            if find == True:
                plist.append(root)
                return find

            if root.right: find = self.searchNode(root.right, node, plist)
            if find == True:
                plist.append(root)
            return find


if __name__ == '__main__':
    t = TreeNode(6)
    t.left = TreeNode(2)
    t.right = TreeNode(8)

    t2 = t.left
    t8 = t.right
    t2.left = TreeNode(0)
    t2.right = TreeNode(4)
    t8.left = TreeNode(7)
    t8.right = TreeNode(9)

    t0 = t2.left
    t0.right = TreeNode(1)

    t4 = t2.right
    t4.left = TreeNode(3)
    t4.right = TreeNode(5)

    so = Solution()
    node = so.lowestCommonAncestor(t, t2, t8)
    print node.val

    plist = []
            
        


