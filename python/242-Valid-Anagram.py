class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        cS: dict[str, int] = {}
        cT: dict[str, int] = {}

        for i in range(len(s)):
            cS[s[i]] = 1 + cS.get(s[i], 0)
            cT[t[i]] = 1 + cT.get(t[i], 0)
        return cS == cT
