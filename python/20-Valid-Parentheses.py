class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        parens: dict[str, str] = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parens.values():
                stack.append(c)
            else:
                if not stack or stack[-1] != parens[c]:
                    return False
                if stack[-1] == parens[c]:
                    _ = stack.pop()
            
        return not stack
