# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == subRoot.val:
                if compareTree(node, subRoot):
                    return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
    
def compareTree(r1, r2) -> bool:
    if not r1 and not r2:
        return True
    if r1 and r2 and r1.val == r2.val:
        return compareTree(r1.left, r2.left) and compareTree(r1.right, r2.right)
    else:
        return False
    
        