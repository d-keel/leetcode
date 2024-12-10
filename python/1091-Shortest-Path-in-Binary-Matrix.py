import collections

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1

        queue = collections.deque([(0, 0, 1)])

        directions: list[tuple[int, int]] = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)]

        grid[0][0] = 1

        while queue:
            x, y, lenn = queue.popleft()

            if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
                return lenn

            for newX, newY in directions:
                newX += x
                newY += y

                if (0 <= newX < len(grid) and (0 <= newY < len(grid[0])) and not grid[newX][newY]):
                    grid[newX][newY] = 1

                    queue.append((newX, newY, lenn + 1))

        return -1

#T: O(n)    n = (rows * cols)
#S: O(n)    n = (rows * cols)
