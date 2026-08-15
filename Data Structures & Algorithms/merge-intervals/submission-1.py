class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        newInterval=intervals[0]
        res=[]
        for i in range(1, len(intervals)):

            if newInterval[1]>=intervals[i][0]:
                newInterval=[min(intervals[i][0], newInterval[0]), max(intervals[i][1],newInterval[1])]
            elif newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                newInterval=intervals[i]
            
        res.append(newInterval)

        return res