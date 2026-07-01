class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        for i in patterns:
            if i in set(word):
                res+=1
        return res
    