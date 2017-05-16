# -*- encoding: utf-8 -*-
'''
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

'''

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    '''
    use queue
    O(n) space
    '''
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root == None:
            return
        
        queue = [root]

        while len(queue) != 0:
            children = []
            h = queue.pop(0)

            if h.left:
                children.append(h.left)
            if h.right:
                children.append(h.right)

            for node in queue:
                h.next = node
                h = node

                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)

            h.next = None

            queue = children

class Solution(object):
    '''
    O(1) space
    two time DFS
    '''
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """

        self.dfs(root)
        self.dfs2(root)

    def dfs(self, root):
        if root == None:
            return

        if root.left != None:
            self.dfs(root.left)
            root.left.next = root.right

        if root.right != None:
            self.dfs(root.right)

    def dfs2(self, root):
        if root == None:
            return

        if root.left != None:
            self.dfs2(root.left)

        if root.right != None:
            if root.next != None:
                root.right.next = root.next.left

            self.dfs2(root.right)

        
if __name__ == '__main__':
    so = Solution()

    root = TreeLinkNode(0)
    root.left = TreeLinkNode(1)
    root.right = TreeLinkNode(2)
    root.left.left = TreeLinkNode(3)
    root.left.right = TreeLinkNode(4)
    root.right.left = TreeLinkNode(5)
    root.right.right = TreeLinkNode(6)

    so.connect(root)

    node = root
    while node != None:
        h = node
        while h != None:
            print h.val,
            h = h.next

        node = node.left
