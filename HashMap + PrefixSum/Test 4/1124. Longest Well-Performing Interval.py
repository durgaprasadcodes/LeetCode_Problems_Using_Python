class Solution:
    def longestWPI(self, nums: List[int]) -> int:
        
        cur_sum = 0
        max_len = 0
        hashmap = {0:-1}
        for idx,num in enumerate(nums):
            cur_sum += 1 if num > 8 else -1
            if cur_sum > 0 :
                max_len = idx+1
            elif  cur_sum - 1 in hashmap:
                max_len = max(max_len,idx-hashmap[cur_sum-1])
                
            if cur_sum not in hashmap:
                hashmap[cur_sum] = idx
        
        return max_len 
