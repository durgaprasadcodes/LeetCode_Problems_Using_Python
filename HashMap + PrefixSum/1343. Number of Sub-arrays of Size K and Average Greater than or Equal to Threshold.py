class Solution:
    def numOfSubarrays(self, nums: list[int], k: int, threshold: int) -> int:
        
        th = threshold*k
        cur_sum = sum(nums[:k])
        ans = 1 if cur_sum >= th else 0
        l = 0
        for num in nums[k:]:
            cur_sum += (-nums[l]+num)
            if cur_sum >= th:
                ans += 1
            l+=1
        return ans