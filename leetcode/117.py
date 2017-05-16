# -*- encoding: utf-8 -*-
'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
'''

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

        if root.right != None:
            if root.next != None and root.right.next == None:
                node = root.next
                while node.left == None and node.right == None and node.next != None:
                    node = node.next

                if node.left != None:
                    root.right.next = node.left
                elif node.right != None:
                    root.right.next = node.right
                else:
                    root.right.next = None

            self.dfs2(root.right)

        if root.left != None:
            if root.next != None and root.left.next == None:
                node = root.next
                while node.left == None and node.right == None and node.next != None:
                    node = node.next

                if node.left != None:
                    root.left.next = node.left
                elif node.right != None:
                    root.left.next = node.right
                else:
                    root.left.next = None

            self.dfs2(root.left)

