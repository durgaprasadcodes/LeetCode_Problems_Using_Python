class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1

        ans = count

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1

            if s[i] in vowels:
                count += 1

            ans = max(ans, count)

            if ans == k:
                return k

        return ans
        
s=Solution()
print(s.maxVowels( "abciiidef", 3))

# TIME COMPLEXITY O(N)
# SPACE COMPLEXITY O(1)