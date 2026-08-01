class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMax, curMin= 1,1
        res=max(nums)

        for n in nums:

            if n==0:
                curMax, curMin = 1,1
                continue

            temp=n*curMax
            curMax=max(temp, n*curMin, n)
            curMin=min(temp, n*curMin, n)

            res=max(res, curMax)

        return res

        # res=nums[0]

        # for i in range(len(nums)):
        #     cur=nums[i]
            
        #     res=max(res, cur)
        #     for j in range(i+1, len(nums)):

        #         cur*=nums[j]

        #         res=max(res, cur)
        # return res
                

    