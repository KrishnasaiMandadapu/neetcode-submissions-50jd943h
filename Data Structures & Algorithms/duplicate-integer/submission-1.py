class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp=[]
        for value in nums:
            if value not in temp:
                temp.append(value)
            else:
                return True
                
        return False
        