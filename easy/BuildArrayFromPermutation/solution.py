from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(0, length):
            nums[i] = nums[i] + (length * (nums[nums[i]] % length))
        for i in range(0, length):
            nums[i] = int(nums[i] / length)
        return nums


if __name__ == '__main__':
    solution = Solution()
    assert (solution.buildArray([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3])
    assert (solution.buildArray([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3])
