class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxArea= 0

        def dfs(i,j):
            if (i <0  or i>= m or j<0 or j >=n or grid[i][j] != 1):
                return 
            else:
                grid[i][j] = 0
                self.island_length += 1
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)

            return self.island_length

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.island_length =0
                    maxArea = max(dfs(i,j), maxArea)

        return maxArea

