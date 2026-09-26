

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = {'a','e','i','o','u'}

        counter = 0
        for i in range(k):
            if s[i] in vowels:
                counter += 1

        best = counter

        for i in range(k, len(s)):
            if s[i] in vowels:
                counter += 1
            
            if s[i - k] in vowels:
                counter -= 1
            
            if counter > best:
                best = counter

        return best
