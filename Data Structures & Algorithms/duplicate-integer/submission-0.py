class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)) :
            for j in range(len(nums)):
                if i != j and nums[j]==nums[i]:
                    return bool(True) 
        return bool(False)