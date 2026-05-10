class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} #number:index

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in seen:
                seen[nums[i]]=i
            else:
                return[seen[complement],i]
        

        
