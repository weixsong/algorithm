# -*- encoding: utf-8 -*-
'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution2(object):
    '''
    merge sort solution
    distributed system
    O(nlogn)
    from bottom to top
    '''
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if lists == None or len(lists) == 0:
            return None

        while len(lists) > 1:
            print len(lists)
            k = 0
            res = []
            while k < len(lists) / 2:
                print k,
                i, j = 2 * k, 2 * k + 1
                l = self.merge(lists[i], lists[j])
                res.append(l)

                k += 1

            if 2 * k <= len(lists) - 1:
                res.append(lists[len(lists) - 1])

            lists = res

        return lists[0]

    def merge(self, l1, l2):
        if l1 == None or l2 == None:
            return l1 or l2

        res = ListNode(0)
        head = res
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next

            res = res.next

        while l1 != None:
            res.next = l1
            l1 = l1.next
            res = res.next

        while l2 != None:
            res.next = l2
            l2 = l2.next
            res = res.next

        return head.next

class Solution1(object):
    '''
    merge sort solution
    distributed system
    O(nlogn)
    from top to bottom
    '''
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == None or len(lists) == 0:
            return lists

        return self.divide(lists, 0, len(lists) - 1)

    def divide(self, lists, left, right):
        if left < right:
            mid = (left + right) / 2
            l1 = self.divide(lists, left, mid)
            l2 = self.divide(lists, mid + 1, right)
            return self.merge(l1, l2)
        else:
            return lists[left]

    def merge(self, l1, l2):
        if l1 == None or l2 == None:
            return l1 or l2

        res = ListNode(0)
        head = res
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next

            res = res.next

        while l1 != None:
            res.next = l1
            l1 = l1.next
            res = res.next

        while l2 != None:
            res.next = l2
            l2 = l2.next
            res = res.next

        return head.next

class Solution(object):
    '''
    Priority Queue
    distributed system
    O(nlogk)
    '''
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        head = ListNode(0)
        p = head

        from heapq import heappush, heappop, heapreplace, heapify
        h = [(node.val, node) for node in lists if node != None]
        heapify(h)

        while len(h) != 0:
            v, node = h[0]

            if node.next == None:
                heappop(h)
            else:
                heapreplace(h, (node.next.val, node.next))

            p.next = node
            p = p.next
            

        return head.next

if __name__ == '__main__':
    so = Solution()

    a1 = ListNode(1)
    b1 = ListNode(0)

    node = so.mergeKLists([a1, b1])
    while node != None:
        print node.val
        node = node.next


