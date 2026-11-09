# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        idx = count - n
        curr = head
        if idx == 0:
            head = head.next
            return head
        while idx > 1:
            curr = curr.next
            idx -= 1
        curr.next = curr.next.next
        return head
        

