class Solution:

    def encode(self, strs: list[str]) -> str:
        out: str = ''
        for s in strs:
            out += str(len(s)) + ':' + s

        return out

    def decode(self, s: str) -> list[str]:
        out: list[str] = []
        l = 0

        while l < len(s):
            r: int = l
            while s[r] != ':':
                r += 1
            
            lenn: int = int(s[l:r ])

            l = r + 1
            r = l + lenn
            out.append(s[l:r])
            l = r

        return out
#T: O(m), m = sum(len(n)), n = len(strs)
#S: O(1)
