class Solution(object):
    def isPalindrome(self, s):
        i=0
        j=len(s)-1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                print(s[i], s[j], i, j)  # debug
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1

        return True
s=Solution()
print(s.isPalindrome ("A man, a plan, a canal: Panami"))

# Time Complexity: O(n)
# Space Complexity: O(1)