class Solution1:
    def numberOfSubstrings(self, s: str) -> int:

        a = b = c = 0
        ans = 0
        l = 0
        n = len(s)
        for r, ch in enumerate(s):
            if ch == "a":
                a += 1
            elif ch == "b":
                b += 1
            else:
                c += 1
            while a and b and c:
                ans += n - r
                if s[l] == "a":
                    a -= 1
                elif s[l] == "b":
                    b -= 1
                else:
                    c -= 1
                l += 1
        return ans


class Solution2:
    def numberOfSubstrings(self, s: str) -> int:

        freq = {}
        ans = 0
        l = 0
        n = len(s)
        for r, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            while len(freq) == 3:
                ans += n - r
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
        return ans
