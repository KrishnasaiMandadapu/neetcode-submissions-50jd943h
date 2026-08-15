"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # intervals.sort(key=lambda i: i.start)
        
        # if len(intervals)==0:
        #     return 0

        # def minRooms(intervals):
        #     res=[]
        #     prevEnd=intervals[0].end
        #     for i in range(1, len(intervals)):

        #         if intervals[i].start>=prevEnd:
        #             prevEnd=intervals[i].end
        #         else:
        #             res.append(intervals[i])
        #             prevEnd=min(intervals[i].end, prevEnd)
        #     return res
        
        # res=minRooms(intervals)
        start=sorted([i.start for i in intervals])
        end=sorted([i.end for i in intervals])

        res,count=0,0
        s,e=0,0
        while(s<len(intervals)):
            if start[s]<end[e]:
                s+=1
                count+=1
            else:
                count-=1
                e+=1
            res=max(res,count)

        return res
       

