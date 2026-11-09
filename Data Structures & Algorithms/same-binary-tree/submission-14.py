class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s1, s2 = [p], [q]
        while s1 and s2:
            n1 = s1.pop()
            n2 = s2.pop()

            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None or n1.val != n2.val:
                return False
            
            s1.append(n1.left)
            s1.append(n1.right)
            s2.append(n2.left)
            s2.append(n2.right)

        return True

            