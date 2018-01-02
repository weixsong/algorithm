# Symmetric Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
        
        queue = [root]
        while len(queue) != 0:
            left, right = 0, len(queue) - 1
            while left <= right:
                if queue[left] is None and queue[right] is None:
                    left += 1
                    right -= 1
                    continue
                elif queue[left] is None or queue[right] is None:
                    return False
                elif queue[left].val != queue[right].val:
                    return False
                left += 1
                right -= 1

            new_queue = []
            for node in queue:
                if node is None:
                    continue
                    
                new_queue.append(node.left)
                new_queue.append(node.right)
                
            queue = new_queue

        return True
