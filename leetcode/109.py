# -*- encoding: utf-8 -*-
'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        nodes = []

        while head != None:
            nodes.append(head.val)
            head = head.next

        left, right = 0, len(nodes) - 1

        return self.build_tree(nodes, left, right)

    def build_tree(self, nodes, left, right):
        if left > right:
            return None

        mid = left + (right - left) / 2
        tree_node = TreeNode(nodes[mid])
        tree_node.left = self.build_tree(nodes, left, mid - 1)
        tree_node.right = self.build_tree(nodes, mid + 1, right)

        return tree_node

if __name__ == '__main__':
    l = ListNode(3)
    l.next = ListNode(5)
    l.next.next = ListNode(8)

    so = Solution()
    t = so.sortedListToBST(l)
    print t.left.val
    print t.val
    print t.right.val


