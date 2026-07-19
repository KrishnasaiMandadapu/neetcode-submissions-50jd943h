class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols=len(heights), len(heights[0])

        pac, atl =set(), set()
        def dfs(r,c, previousHeight, visit):

            if (r<0 or c<0 or r==rows or c==cols or heights[r][c]<previousHeight
            or (r,c) in visit):
                return 

            visit.add((r,c))

            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                dfs(r+dr, c+dc, heights[r][c], visit)


        res=[]
        for c in range(cols):
            dfs(0,c,heights[0][c],pac)
            dfs(rows-1, c, heights[rows-1][c], atl)
        
        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols-1, heights[r][cols-1], atl)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in atl and (r,c) in pac:
                    res.append([r,c])
        return res
