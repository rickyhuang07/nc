class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self, w):
        cur = self
        for c in w:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        res = set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in node.children or (r, c) in visited:
                return 
            visited.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.isEnd:
                res.add(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))
            
                
            
        root = TrieNode()
        for word in words:
            root.addWord(word)
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "")
        return list(res)