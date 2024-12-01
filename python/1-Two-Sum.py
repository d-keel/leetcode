class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap: dict[int, int] = {} 
        sol: list[int] = []

        for i, n in enumerate(nums):
            diff = target - n
            if diff in numMap:
                sol = [numMap[diff], i]
                break
            numMap[n] = i

        return sol
