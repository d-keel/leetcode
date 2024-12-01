class Solution:
    def trap(self, height: list[int]) -> int:
        lp: int = 0
        rp: int = len(height) - 1
        maxLeft: int = height[lp]
        maxRight: int = height[rp]
        water: int = 0

        while lp < rp:
            if maxLeft < maxRight:
                lp += 1
                maxLeft = max(maxLeft, height[lp])
                water += maxLeft - height[lp]
            else:
                rp -= 1
                maxRight = max(maxRight, height[rp])
                water += maxRight - height[rp]

        return water
