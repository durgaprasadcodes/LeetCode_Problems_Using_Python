# =============== OPTIMAL SOLUTION =============
class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        
        n = len(boxes)
        if n == 1:
            return [0]

        ans = []
        total_ones = 0
        right_indices_sum = 0

        for idx,num in enumerate(boxes):
            if num == '1':
                total_ones += 1 
                right_indices_sum += idx 
        
        left_ones = right_ones = 0
        left_indices_sum = 0

        for idx,num in enumerate(boxes):

            right_ones = total_ones - left_ones - int(num)

            if num == '1':
                left_ones += 1 
                left_indices_sum += idx
                right_indices_sum -= idx


            cost = ( 
                    idx*left_ones - left_indices_sum 
                    +
                    right_indices_sum - idx*right_ones
                )
            ans.append(cost)
        return ans

# =============== BRUTE FORCE ==================
class Solution:

    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        if n == 1:
            return [0]

        ans = []
        for i in range(len(boxes)):
            cur_ans = 0
            for j in range(len(boxes)):
                if i != j and boxes[j] == "1":
                    cur_ans += abs(j - i)
            ans.append(cur_ans)

        return ans
