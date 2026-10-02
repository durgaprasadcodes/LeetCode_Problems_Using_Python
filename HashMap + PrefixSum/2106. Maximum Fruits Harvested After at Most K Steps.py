class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], start_pos: int, k: int) -> int:
        
        l = 0
        max_sum = cur_sum = 0
        for r in range(len(fruits)):
            cur_sum += fruits[r][1]

            left_pos = fruits[l][0]
            right_pos = fruits[r][0]

            if right_pos <= start_pos:
                cost = start_pos - left_pos
            elif left_pos >= start_pos:
                cost = right_pos - start_pos
            else:
                cost = min(
                    (start_pos - left_pos) + (right_pos - left_pos),
                    (right_pos - start_pos) + (right_pos - left_pos)
                )

            while  cost > k:
                cur_sum -= fruits[l][1]
                l+=1

                if l > r:
                    break
                    
                left_pos  = fruits[l][0]
                right_pos = fruits[r][0]
                
                if right_pos <= start_pos:
                    cost = start_pos - left_pos
                elif left_pos >= start_pos:
                    cost = right_pos - start_pos
                else:
                    cost = min(
                        (start_pos - left_pos) + (right_pos - left_pos),
                        (right_pos - start_pos) + (right_pos - left_pos)
                    )
            max_sum = max(max_sum,cur_sum)

        return max_sum
                                                                        