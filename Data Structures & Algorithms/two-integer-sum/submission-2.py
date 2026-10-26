class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # number:index

        for i, num in enumerate(nums):
            comp = target - num

            if comp in seen:
                return [seen[comp], i] #return comp first bcoz here is obv the smaller index since its in seen.
            else:
                seen[num] = i

            