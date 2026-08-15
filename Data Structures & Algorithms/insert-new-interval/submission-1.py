class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res=[]
        Flag=True
        for k in range(len(intervals)):
            i,j=intervals[k][0], intervals[k][1]

            if newInterval[0]>j:
                res.append([i,j])
                
            elif (newInterval[1]<i):
                res.append(newInterval)
                return res+intervals[k:]
            else:
                newInterval=[min(i, newInterval[0]), max(j, newInterval[1])]

        res.append(newInterval)
                


        return res

