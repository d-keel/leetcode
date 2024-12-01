class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        sett: set[str] = set()
        maxx: int = 0
        left: int = 0
        right: int = left + 1
        sett.add(s[left])

        while left < len(s):
            if right < len(s) and s[right] not in sett:
                sett.add(s[right])
                right += 1
            else:
                sett.discard(s[left])
                left += 1 
            maxx = max(maxx, len(sett))

        return maxx
