# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 == None: return l2
        if l2 == None: return l1
        
        head = res = ListNode(0)
        carrier = 0
        
        while l1 != None and l2 != None:
            val = l1.val + l2.val + carrier
            carrier = val / 10
            val = val % 10
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next
            l2 = l2.next
            
        while l1 != None:
            val = l1.val + carrier
            carrier = val / 10
            val = val % 10
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next
            
        while l2 != None:
            val = l2.val + carrier
            carrier = val / 10
            val = val % 10
            head.next = ListNode(val)
            head = head.next
            l2 = l2.next
            
        if carrier != 0:
            head.next = ListNode(carrier)
            
        return res.next