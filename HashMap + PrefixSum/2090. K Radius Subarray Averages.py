class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums 
        n = len(nums) 
        window_size = 2*k+1
        ans = [-1]*n
        if n < window_size:
            return ans
        window_sum = sum(nums[:window_size])
        ans[k] = window_sum//window_size
        l = 0
        for i in range(k+1,n-k):
            window_sum += -nums[l] + nums[i+k]
            ans[i] = window_sum//window_size
            l+=1 
        return ans


# class Solution:
#     def getAverages(self, nums: list[int], k: int) -> list[int]:
        
#         if k == 0:
#             return nums

#         n = len(nums)
#         if k > n:
#             return [-1]*n

#         prefix_sum = []
#         cur_sum = 0
#         for num in nums:
#             cur_sum += num
#             prefix_sum.append(cur_sum)

#         cur_sum = 0
#         res = []
#         l = 0
#         for i in range(n):
#             if i-k < 0 or i+k >= n:
#                 res.append(-1)
#             else:
#                 if i-k==0:
#                     avg = ( prefix_sum[i+k] )//(2*k+1)
#                 else:
#                     avg = (-prefix_sum[i-k-1] + prefix_sum[i+k] )//(2*k+1)
#                 res.append(avg)
#         return res
