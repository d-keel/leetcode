class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        total: int = sum(nums)
        if total % 2 != 0:
            return False

        possiblesums: set[int] = set()
        target = total / 2

        for i in range(len(nums)):
            if nums[i] == target:
                return True
            #nums[i] contains possible sums
            newsums = set([nums[i]])
            for s in possiblesums:
                if s+nums[i] == target:
                    return True
                if s+nums[i] < target:
                    newsums.add(s+nums[i])
            possiblesums = possiblesums.union(newsums)

        return False
