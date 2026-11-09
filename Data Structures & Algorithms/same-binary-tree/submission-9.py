# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        dq1 = deque()
        dq2 = deque()
        if p:
            dq1.append(p)
        if q:
            dq2.append(q)
        while dq1 and dq2:
            n1 = dq1.popleft()
            n2 = dq2.popleft()
            if n1 and not n2 or (n2 and not n1):
                return False
            elif (not n1 and not n2) or n1.val == n2.val:
                if n1 and n2:
                    dq1.append(n1.left)
                    dq1.append(n1.right)
                    dq2.append(n2.left)
                    dq2.append(n2.right)
            else:
                return False
        if dq1 or dq2:
            return False
        return True
         
