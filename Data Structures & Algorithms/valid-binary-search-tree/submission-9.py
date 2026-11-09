# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        range = (float('-inf'), float('inf'))
        return self.dfs(root, range)

    def dfs(self, root, range):
            if root and root.val > range[0] and root.val < range[1]:
                return self.dfs(root.left, (range[0], root.val)) and self.dfs(root.right, (root.val, range[1]))
            elif not root:
                return True
            else:
                return False
          
            