# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode],res=None) -> Optional[ListNode]:
        s = []
        while head:
            s.append(head.val)                        
            head =head.next
        res = None
        if s:
            res = new = ListNode(s.pop())
        while s:
            new.next = ListNode(s.pop())
            new = new.next
        
        return res 
