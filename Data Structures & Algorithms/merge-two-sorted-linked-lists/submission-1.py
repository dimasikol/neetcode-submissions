# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new = None
        res = None
        left = 0
        right = 0 
        while list1 and list2:
            if list1.val > list2.val:
               q = ListNode(list2.val)
               list2 = list2.next
            else:
               q = ListNode(list1.val)    
               list1 = list1.next
            if new == None:
                new = q
                res = q
            else:
                new.next = q
                new = new.next
        if list2:
            list1 = list2 
        while list1:
            if new == None:
                new = ListNode(list1.val)
                res = new
            else:
                new.next = ListNode(list1.val)
                new = new.next
            list1 = list1.next
        return res