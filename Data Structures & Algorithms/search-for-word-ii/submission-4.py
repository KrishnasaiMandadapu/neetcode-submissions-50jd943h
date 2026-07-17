class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

    def insertWord(self,word):
        cur=self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch]=TrieNode()
            cur=cur.children[ch]
        cur.end=True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root=TrieNode()
        for word in words:
            root.insertWord(word)
            
        rows, col = len(board), len(board[0])
        path, res = set(), set()

        def dfs(r, c, node,word):

            if (r < 0 or c < 0 or
                r >= rows or c >= col or
                (r, c) in path or
                board[r][c] not in node.children):
                return 
        
       
        
            path.add((r, c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.end:
                res.add(word)
        
            
            dfs(r+1, c, node, word) 
            dfs(r-1, c, node, word) 
            dfs(r, c+1, node, word) 
            dfs(r, c-1, node, word)
            
        
            path.remove((r, c))
          

    

       
        for r in range(rows):
            for c in range(col):
                dfs(r,c,root,"")
                        

        return list(res)
