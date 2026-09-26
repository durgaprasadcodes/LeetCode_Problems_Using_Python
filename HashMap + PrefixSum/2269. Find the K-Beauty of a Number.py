class Solution:
    def divisorSubstrings(self, number: int, k: int) -> int:
        string_num = str(number)
        K_Beauty = 0
        l = 0
        for r in range(k,len(string_num)+1):
            num = string_num[l:r]
            integer = int(num)
            if integer and  number%integer == 0:
                K_Beauty += 1
            l+=1
        return K_Beauty
        # string_num = str(number)
        # K_Beauty = 0
        # formatted_num = ""
        # for num in string_num:
        #     formatted_num += num
        #     if len(formatted_num) == k:
        #         formatted_number = int(formatted_num)
        #         if formatted_number and  number % formatted_number == 0:
        #             K_Beauty += 1
        #         formatted_num = formatted_num[1:]
        # return K_Beauty