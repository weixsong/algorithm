# Symmetric Tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''layer wise traverse'''
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


class Solution2(object):
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
