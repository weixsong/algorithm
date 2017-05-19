# -*- encoding: utf-8 -*-
'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

Try to utilize the property of a BST.
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST).

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        self.visited = 0
        return self.findk(root, k).val

    def findk(self, root, k):
        if root == None:
            return None

        node = self.findk(root.left, k)
        if node:
            return node

        self.visited += 1
        if self.visited == k:
            return root

        node = self.findk(root.right, k)
        return node


class Solution1(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        self.size(root)
        return self.findk(root, k).val

    def findk(self, root, k):
        a = 0
        if root.left:
            a = root.left.size

        if a == k - 1:
            return root

        if a >= k:
            return self.findk(root.left, k)

        if a < k - 1:
            return self.findk(root.right, k - a - 1)

    def size(self, root):
        if root == None:
            return 0

        root.size = 1 + self.size(root.left) + self.size(root.right)
        return root.size


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.visited = 0
        self.rank(root)

        while root != None and root.rank != k:
            if k < root.rank:
                root = root.left
            if k > root.rank:
                root = root.right

        return root.val

    def rank(self, root):
        if root == None:
            return

        self.rank(root.left)
        self.visited += 1
        root.rank = self.visited
        self.rank(root.right)


if __name__ == '__main__':
    so = Solution()

    root = TreeNode(8)
    root.left = TreeNode(6)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)

    root.right = TreeNode(10)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(12)

    so.kthSmallest(root, 3)

    queue = [root]

    while len(queue) != 0:
        front = queue.pop(0)
        print front.rank

        if front.left != None:
            queue.append(front.left)

        if front.right != None:
            queue.append(front.right)

    print '**************************'
    print so.kthSmallest(root, 5)


