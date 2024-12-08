class Solution:
    def isValid(self, left: int, right: int, s: str) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left: int = 0
        right: int = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.isValid(left + 1, right, s)\
                    or self.isValid(left, right - 1, s)
            left += 1
            right -= 1

        return True

#T: O(n)    n = len(s)
#S: O(1)
