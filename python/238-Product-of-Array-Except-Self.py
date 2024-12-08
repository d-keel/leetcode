class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        lenn: int = len(nums)
        out: list[int] = [1] * lenn

        for i in range(1, lenn):
            out[i] = out[i-1] * nums[i - 1]

        suffix: int = 1
        for i in range(lenn - 1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]
        
        return out

#T: O(n)    n = len(nums)
#S: O(1)
