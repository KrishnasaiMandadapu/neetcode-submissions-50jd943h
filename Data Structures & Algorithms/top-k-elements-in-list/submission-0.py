from heapq import nlargest
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newdict=defaultdict(int)
        for value in nums:
            newdict[value]+=1
        topklist=nlargest(k, newdict, key=newdict.get)
        return topklist
        
        
        