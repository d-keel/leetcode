class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack: list[int] = []
        remove: set[int] = set()

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    _ = stack.pop()
                else:
                    remove.add(i)

        while stack:
            remove.add(stack.pop())

        result: list[str] = []
        for i, char in enumerate(s):
            if i not in remove:
                result.append(char)

        return ''.join(result)
