class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands: int = 0

        directions: list[tuple[int, int]] = [(0,1), (-1,0), (1, 0), (0, -1)]

        def zeroize(grid: list[list[str]], r: int, c: int):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0])) and grid[r][c] == '1':
                grid[r][c] = '0'

                for row, col in directions:
                    zeroize(grid, r + row, c + col)
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    zeroize(grid, row, col)
                    
                    islands += 1

        return islands
