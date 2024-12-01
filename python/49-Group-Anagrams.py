class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans: dict[tuple[list[int]], list[str]] = {}

        for s in strs:
            count: list[int] = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if ans.get(tuple(count)):
                ans[tuple(count)].append(s)
            else:
                ans[tuple(count)] = [s]
        return list(ans.values())
