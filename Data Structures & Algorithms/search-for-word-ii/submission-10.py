class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word: str):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        res = set()
        root = TrieNode()
        for word in words:
            root.addWord(word)

        def dfs(r, c, node, curWord):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in node.children or (r, c) in visited:
                return
            visited.add((r, c))
            node = node.children[board[r][c]]
            curWord += board[r][c]
            if node.end:
                res.add(curWord)
            dfs(r + 1, c, node, curWord)
            dfs(r - 1, c, node, curWord)
            dfs(r, c + 1, node, curWord)
            dfs(r, c - 1, node, curWord)
            visited.remove((r, c))

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root, "")
        return list(res)

        

        
        
