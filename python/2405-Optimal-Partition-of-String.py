class Solution(object):
    def partitionString(self, s: str) -> int:
        count: int = 1
        seen: set[str] = set()
        for ch in s:
            if ch not in seen:
                seen.add(ch)
                continue
            seen.clear()
            seen.add(ch)
            count += 1
        return count
