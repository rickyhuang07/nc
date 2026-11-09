# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                res.append(str(node.val))
            else:
                res.append("N")
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        code = data.split(",")
        if code[0] == "N":
            return None
        root = TreeNode(int(code[0]))
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()
            if code[index] == "N":
                node.left = None
            else:
                node.left = TreeNode(code[index])
                q.append(node.left)
            index += 1
            if code[index] == "N":
                node.right = None
            else:
                node.right = TreeNode(code[index])
                q.append(node.right)
            index += 1
        return root


                

        
