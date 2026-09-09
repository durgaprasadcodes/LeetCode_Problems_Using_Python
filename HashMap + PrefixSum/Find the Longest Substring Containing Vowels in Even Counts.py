class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        bits = { 'a':1,'e':2,'i':4,'o':8,'u':16 }

        mask = 0
        max_len = 0
        freq = {0:-1}

        for idx,ch in enumerate(s):
            if ch in bits:
                mask ^= bits[ch]
            if mask in freq:
                max_len = max(max_len,idx-freq[mask])
            else:
                freq[mask] = idx
        return max_len
        
        