class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r-l+1 > len(longest):
                        longest = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break
        
        for i in range(len(s)):
            l = i
            r = i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r-l+1 > len(longest):
                        longest = s[l:r+1]
                    l-=1
                    r+=1
                else:
                    break
        return longest