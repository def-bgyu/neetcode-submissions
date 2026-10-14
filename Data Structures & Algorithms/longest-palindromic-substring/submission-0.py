class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Expand around the center method

        n = len(s)
        maxLen = 1
        start = 0

        for i in range(n): #Every position in the string is a center once
            for j in range(2): 
                low = i
                high = i+j
                # Run twice for each position, when j=0 both pointers are on same position i.e odd, and for even they are next to each other
                while low >= 0 and high < n and s[low] == s[high]:
                    currLen = high - low +1
                    if currLen > maxLen:
                        start = low
                        maxLen = currLen
                    low -= 1
                    high += 1
        return s[start : start + maxLen]
        
