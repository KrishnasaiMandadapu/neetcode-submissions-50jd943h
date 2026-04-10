class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        new_dict={}
        for i,n in enumerate(nums):
            new_dict[n]=i

        for i,n in enumerate(nums):
            diff=target-n
            if diff in new_dict and new_dict[diff]!=i:
                return [i, new_dict[diff]]
        return []