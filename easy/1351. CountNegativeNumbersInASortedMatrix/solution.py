from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row_length = len(grid[0])
        negative_count = 0
        for row_idex in range(len(grid) - 1, -1, -1):
            right = row_length - 1
            while grid[row_idex][right] < 0:
                right -= 1
                if grid[row_idex][right] >= 0:
                    negative_count += row_length - right - 1
                    break
                if right == -1:
                    negative_count += row_length
                    break
        return negative_count


if __name__ == '__main__':
    solution = Solution()
    assert (solution.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8)
    assert (solution.countNegatives([[3, 2], [1, 0]]) == 0)
