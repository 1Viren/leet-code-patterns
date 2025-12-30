class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        for r in range(rows - 2):
            for c in range(cols - 2):

                if grid[r + 1][c + 1] != 5:
                    continue

                used = set()
                valid = True

                for i in range(3):
                    for j in range(3):
                        val = grid[r + i][c + j]
                        if val < 1 or val > 9 or val in used:
                            valid = False
                            break
                        used.add(val)
                    if not valid:
                        break

                if not valid:
                    continue

                for i in range(3):
                    s = 0
                    for j in range(3):
                        s += grid[r + i][c + j]
                    if s != 15:
                        valid = False
                        break

                if not valid:
                    continue

                for j in range(3):
                    s = 0
                    for i in range(3):
                        s += grid[r + i][c + j]
                    if s != 15:
                        valid = False
                        break

                if not valid:
                    continue

                s = 0
                for i in range(3):
                    s += grid[r + i][c + i]
                if s != 15:
                    continue

                s = 0
                for i in range(3):
                    s += grid[r + i][c + 2 - i]
                if s != 15:
                    continue

                result += 1

        return result   
