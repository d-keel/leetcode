class Solution(object):
    def containsDuplicate(self, nums: list[int]) -> bool:
        A: set[int] = set()
        for i in nums:
            if i in A:
                return True
            A.add(i)
        return False
