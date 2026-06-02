class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        if k==1:
            return max(arr)
        if k==len(arr):
            return sum(arr)
        curr_len=actual_len=sum(arr[:k])
        j=0
        for i in range(k,len(arr)):
            curr_len=curr_len-arr[j]+arr[i]
            actual_len=max(actual_len,curr_len)
            j+=1
        return actual_len
    
s=Solution()
print(s.maxSubarraySum([1,2,3,4,5], 2 ))