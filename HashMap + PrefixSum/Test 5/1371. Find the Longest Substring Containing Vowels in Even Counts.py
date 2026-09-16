def findTheLongestSubstring(self, s: str) -> int:
        bits = {
            'a': 2,
            'e': 4,
            'i': 8,
            'o': 16,
            'u': 32
        }
        ans = 0
        table = {0:-1}
        xor = 0
        for idx,ch in enumerate(s):
            if ch in bits:
                xor ^= bits[ch]
            if xor in table:
                ans = max(ans,idx-table[xor])
            else:
                table[xor] = idx
        return ans