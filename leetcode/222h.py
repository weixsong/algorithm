# -*- encoding: utf-8 -*-
'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    over time
    '''
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0

        q = [root]
        count = 0
        while len(q) != 0:
            front = q.pop(0)
            count += 1

            if front.left != None:
                q.append(front.left)

            if front.right != None:
                q.append(front.right)

        return count

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        lh = self.left_depth(root)
        rh = self.right_depth(root)

        if lh == rh:
            return 2 ** lh - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def left_depth(self, node):
        depth = 0
        while node != None:
            depth += 1
            node = node.left

        return depth

    def right_depth(self, node):
        depth = 0
        while node != None:
            depth += 1
            node = node.right

        return depth







