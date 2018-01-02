# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root == None:
            return root
        
        if root.left is not None or root.right is not None:
            root.left, root.right = root.right, root.left
            
        if root.left is not None:
            self.invertTree(root.left)
        
        if root.right is not None:
            self.invertTree(root.right)
            
        return root


class Solution2(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root == None:
            return root
        
        queue = [root]
        
        while len(queue) != 0:
            front = queue.pop(0)
            if front.left or front.right:
                front.left, front.right = front.right, front.left
                
            if front.left:
                queue.append(front.left)
                
            if front.right:
                queue.append(front.right)
            
        return root
