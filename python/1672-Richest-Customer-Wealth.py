class Solution(object):
    def maximumWealth(self, accounts: list[list[int]]):
        maxx: int = 0
        for customer in accounts:
            cSum: int = 0
            for bank in customer:
                cSum += bank
            maxx = max(maxx, cSum)

        return maxx
