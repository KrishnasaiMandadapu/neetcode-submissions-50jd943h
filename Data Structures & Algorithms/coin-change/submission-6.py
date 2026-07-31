class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp=[amount+1]*(amount+1)
        dp[0]=0

        for a in range(1, amount+1):
            for coin in coins:
                if a-coin>=0:
                    dp[a]=min(dp[a],1+dp[a-coin])
        
        return dp[amount] if dp[amount]!=amount+1 else -1
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     cache={}
    #     temp=amount+1
    #     def dfs(amount):
    #         if amount==0:
    #             return 0
            
    #         if amount in cache:
    #             return cache[amount]
    #         res=temp
    #         for coin in coins:
    #             if amount-coin>=0:
    #                 res=min(res,1+dfs(amount-coin))
    #         cache[amount]=res

    #         return res

    #     mincoins=dfs(amount)

    #     return mincoins if mincoins<temp else -1


    


