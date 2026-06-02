class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        l=0
        max_len=0
        min_freq=0
        countT=countF=0
        for r in range(len(answerKey)):
            if answerKey[r]=='T':
                countT+=1
            else:
                countF+=1
            while min(countT,countF)>k:
                if answerKey[l]=='T':
                    countT-=1
                else:
                    countF-=1
                l+=1
            max_len=max_len if max_len > (r-l+1) else r-l+1
        return max_len
    
s=Solution()
print(s.maxConsecutiveAnswers("TTFF", 2))

# Time Complexity: O(n)
# Space Complexity: O(1)