import random

class Solution:

    def __init__(self, w: list[int]):
        self.preSum: list[int] = []
        self.totalSum: int = 0

        for weight in w:
            self.totalSum += weight
            self.preSum.append(self.totalSum)

    def pickIndex(self) -> int:
        target: int = random.randint(1, self.totalSum)
        
        l: int = 0
        r: int = len(self.preSum)

        while l < r:
            mid = (l + r) // 2

            if self.preSum[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l
