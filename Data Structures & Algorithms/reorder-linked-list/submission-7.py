# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        l1 = head
        l2 = slow.next
        slow.next = None
        prev = None
        # reverse order of second half:
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        
        l2 = prev
        curr = ListNode()
        while l2:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
            curr.next = l2
            curr = curr.next
            l2 = l2.next
        if l1:
            curr.next = l1

        