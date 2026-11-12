class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        table = {"{": "}", "[": "]", "(": ")"}
        stack = []

        for b in s:
            if b in table:
                stack.append(b)
            else:
                if not stack:
                    return False
                poped = stack.pop()
                if table[poped] != b:
                    return False

        return True if not stack else False
