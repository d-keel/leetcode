class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, str(s.lower())))

        return s == s[::-1]
