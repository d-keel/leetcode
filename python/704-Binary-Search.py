class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l: int = 0
        r: int = len(nums) - 1

        while l <= r:
            m: int = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1

# T: O(logn)    n = len(nums)
# S: O(1)
