class Solution:
    def findSubstring(self, s: str, words):
        from collections import defaultdict
        if not s or not  words:
            return []
        word_length  = len(words[0])
        total_length = len(words)
        res=[]
        original_freq = defaultdict(int)
        for word in words:
            original_freq[word]+=1
        original_freq_length = len(original_freq)
        for i in range( word_length ):
            current_freq = defaultdict(int)
            valid = 0
            l=i
            count=0
            for r in range(i,len(s)-word_length+1,word_length):
                subString = s[r:r+word_length]
                if subString not in original_freq:
                    current_freq.clear()
                    valid=count=0
                    l=r+word_length
                    continue
                current_freq[subString]+=1
                count+=1
                if current_freq[subString] == original_freq[subString] :
                    valid+=1
                while current_freq[subString]>original_freq[subString]:
                    currString = s[l:l+word_length]
                    if current_freq[currString] == original_freq[currString] :
                        valid-=1
                    current_freq[currString]-=1
                    count-=1
                    l+=word_length
                print(subString,valid,count)
                if count == total_length and valid == original_freq_length:
                    res.append(l)
        return res

s=Solution()
print(s.findSubstring( "barfoothefoobarman",["foo","bar"]))

# Time Complexity O(W*K + N), where N is the length of string s, W is the total number of words, and K is the length of each individual word.
# Space Complexity O(W*K) where W is the number of words in the words list and K is the length of a single word.