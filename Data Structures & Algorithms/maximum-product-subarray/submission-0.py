class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = 1
        curMin = 1
        result = nums[0]

        for n in nums:
            temp = curMax * n         

            curMax = max(temp , n ,curMin * n )
            curMin = min(temp , n ,curMin * n )

            result = max(result, curMax)

        return result       