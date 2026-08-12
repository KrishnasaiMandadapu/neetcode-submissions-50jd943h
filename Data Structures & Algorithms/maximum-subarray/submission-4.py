class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res, temp=nums[0],0
        for i in range(len(nums)):
            
            if temp<0:
                temp=0
            temp+=nums[i]
            res=max(temp, res)
        return res


