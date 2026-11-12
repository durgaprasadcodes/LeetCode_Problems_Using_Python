class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) == 1:
            return s

        stack = []
        for ch in s:
            if stack and ch == stack[-1]:
                while stack and ch == stack[-1]:
                    stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
            