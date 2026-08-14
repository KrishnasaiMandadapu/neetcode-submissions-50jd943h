class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # goal = len(nums)-1
        # for i in range(len(nums)-1,-1,-1):

        #     if i+nums[i]>=goal:
        #         goal=i

        # return goal==0

        cache={}
        
        def dfs(i):

            if i in cache:
                return cache[i]
            if i==len(nums)-1:
                return True
            if nums[i]==0:
                return False
            end=min(len(nums)-1, nums[i]+i)
            for j in range(i+1, end+1):
                if dfs(j):
                    cache[i]=True
                    return True
            cache[i]=False
            return False

        return dfs(0)
            




        

