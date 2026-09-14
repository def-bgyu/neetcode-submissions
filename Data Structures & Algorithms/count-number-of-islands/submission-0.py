class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_islands = 0

        def dfs(i,j):
            if (i < 0 or i >= m or j <0 or j >= n or grid[i][j] != "1"):
                return 
            else:
                grid[i][j] = "0"
                dfs(i+1, j) #explore all 4 directions
                dfs(i, j+1)
                dfs(i-1,j)
                dfs(i, j-1)

        if m == 0:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i,j)
        return num_islands



        
                
        