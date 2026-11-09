# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1001)
        for i in range (len(lists)):
            cur = dummy
            newHead = lists[i]
            while newHead and cur.next:
                if newHead.val < cur.next.val:
                    temp = newHead.next
                    newHead.next = cur.next
                    cur.next = newHead
                    cur = cur.next
                    newHead = temp
                else:
                    cur = cur.next
            if newHead:
                cur.next = newHead

        return dummy.next
            

            
            

        
        