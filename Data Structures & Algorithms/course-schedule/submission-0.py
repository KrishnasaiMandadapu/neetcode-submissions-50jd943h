class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hashset={i:[] for i in range(numCourses)}
        for cour, pre in prerequisites:
            hashset[cour].append(pre)

        visit=set()
        def dfs(c):
            if c in visit:
                return False
            
            if hashset[c]==[]:
                return True

            visit.add(c)
            for pre in hashset[c]:
                if not dfs(pre):
                    return False
                
            visit.remove(c)
            hashset[c]=[]
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True
            