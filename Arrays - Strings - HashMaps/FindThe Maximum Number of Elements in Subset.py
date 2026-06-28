class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans=1
        for num in freq.keys():
            if num == 1:
                if not freq[1]%2:
                    ans = ans = max(ans,freq[1]-1)
                else:
                    ans = ans = max(ans,freq[1])
            else:
                length = 0
                temp = num
                while temp in freq and freq[temp]>=2:
                    length+=2
                    temp*=temp
                if temp in freq and freq[temp] == 1 :
                    length+=1
                else:
                    length-=1

                ans = max(ans,length)
        return ans            
        