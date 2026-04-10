class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,output=[],[]
        temp=1
        for i in range(len(nums)):
            prefix.append(temp*nums[i])
            temp*=nums[i]
        
        post=1
        for j in range(len(nums)-1,-1,-1):
            if j==0:
                output.append(post)
            else:
                output.append(post*prefix[j-1])

            post*=nums[j]
        
        return output[::-1]
