"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visit={}
        def bfs(node):

            q=collections.deque([node])
             
            while q:

                popedNode=q.popleft()
                if popedNode in visit:
                    return visit[popedNode]

                copy=Node(popedNode.val)
                visit[node]=copy
                for nei in popedNode.neighbors:
                    copy.neighbors.append(bfs(nei))
                
            return copy
        return bfs(node) if node else None