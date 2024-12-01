class Solution(object):
    def kthFactor(self, n: int, k: int) -> int:
        factors: list[int] = []
        factors.append(1)
        for i in range(2, n):
            if (n % i == 0):
                factors.append(i)
        factors.append(n)
        try:
            return factors[k-1]
        except IndexError:
            return -1
