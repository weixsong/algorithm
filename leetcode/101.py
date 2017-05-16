# -*- encoding: utf-8 -*-
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    recursive
    '''
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.symmetric(root.left, root.right)

    def symmetric(self, p, q):
        if p == None and q == None:
            return True

        if p != None and q != None:
            if p.val == q.val:
                return self.symmetric(p.left, q.right) and self.symmetric(p.right, q.left)
            else:
                return False

        return False


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root == None:
            return True

        stack1 = [root.left]
        stack2 = [root.right]

        while len(stack1) != 0 and len(stack2) != 0:
            t1 = stack1.pop()
            t2 = stack2.pop()
            
            if t1 == None and t2 == None:
                continue
            elif t1 != None and t2 != None:
                if t1.val != t2.val:
                    return False

                stack1.append(t1.left)
                stack2.append(t2.right)

                stack1.append(t1.right)
                stack2.append(t2.left)
            else:
                return False

        if len(stack1) != len(stack2):
            return False
        return True
