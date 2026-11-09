# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fastptr = head
        slowptr = head
        while fastptr.next and fastptr.next.next and fastptr.next.next != slowptr.next:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
        
        if not fastptr.next or not fastptr.next.next:
            return False
        return True
        
        