'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        p = head

        i = 0
        while i < n:
            p = p.next
            i += 1

        pre = head
        while p!= None and p.next != None:
            p = p.next
            pre = pre.next

        if p == None:
            head = head.next
        else:
            pre.next = pre.next.next

        return head

if __name__ == '__main__':
    so = Solution()

    n1 = ListNode(1)
    n2 = ListNode(2)
