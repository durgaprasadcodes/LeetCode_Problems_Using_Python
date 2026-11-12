class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows == 1:
            return s
        res = [""]*numRows
        direction = 1
        row = 0
        for ch in s:
            res[row]+=ch
            if row == 0:
                d = 1
            if row == numRows-1 :
                d = -1
            row += d
        return "".join(res)
    
s = Solution()
print(s.convert("PAYPALISHIRING",3))