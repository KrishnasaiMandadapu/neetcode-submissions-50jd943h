class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges)!=n-1:
            return False

        if not n:
            return True

        prehash={i:[] for i in range(n)}
        for node1, node2 in edges:
            prehash[node1].append(node2)
            prehash[node2].append(node1)

        visit=set()
        def dfs(prev,node):

            if node in visit:
                return False
            
            visit.add(node)
            for nei in prehash[node]:
                if nei==prev:
                    continue
                if not dfs(node, nei):
                    return False

            return True

        return dfs(-1,0) and len(visit)==n