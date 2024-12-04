class Solution:
    def customSortString(self, order: str, s: str) -> str:
        out: str = ''
        hashMap: dict[str, int] = {}

        for key in s:
            if key in hashMap:
                hashMap[key] += 1
            else:
                hashMap[key] = 1

        for i in order:
            if i in s:
                for key in hashMap:
                    if i == key:
                        out += i * hashMap[key]
        
        for i in s:
            if i not in out:
                for key in hashMap:
                    if i == key:
                        out += i * hashMap[key]

        return out
