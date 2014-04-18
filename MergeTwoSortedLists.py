"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if l1.val > l2.val:
                l = l2
                l2 = l2.next
            else:
                l = l1
                l1 = l1.next
            res = l
            while l1 and l2:
                if l1.val > l2.val:
                    l.next = l2
                    l = l.next
                    l2 = l2.next
                else:
                    l.next = l1
                    l = l.next
                    l1 = l1.next
            while l1:
                l.next = l1
                l = l.next
                l1 = l1.next
            while l2:
                l.next = l2
                l = l.next
                l2 = l2.next
            return res
                    