class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i >= len(nums) or i < 0:
                return 0
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1)) #Choice to either rob or just skip it
                return memo[i]

        return max(dfs(0), dfs(1))
