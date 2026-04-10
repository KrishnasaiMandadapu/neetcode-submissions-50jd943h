class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet=set(nums)
        long=0
        for i in nums:
            if i-1 not in newSet:
                l=0
                while i+l in newSet:
                    l+=1
                long=max(l, long)
        return long

