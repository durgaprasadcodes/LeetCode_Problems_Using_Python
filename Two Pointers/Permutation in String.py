class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2) or len(s2)=="" :
            return  False
        s1_freq=[0]*26
        s2_freq=[0]*26
        
        for i in s1:
            s1_freq[ord(i)-97]+=1

        for i in s2[:len(s1)]:
            s2_freq[ord(i)-97]+=1

        if s1_freq == s2_freq:
            return True
        
        for i in range(len(s1),len(s2)):
            s2_freq[ord(s2[i-len(s1)])-97]-=1
            s2_freq[ord(s2[i])-97]+=1
            if s1_freq==s2_freq:
                return True
        return False

s=Solution()
print(s.checkInclusion("ab","eidbaooo"))

# Time Complexity: O(n) where n is the length of s2
# Space Complexity: O(1) since the frequency arrays have a fixed size of 26