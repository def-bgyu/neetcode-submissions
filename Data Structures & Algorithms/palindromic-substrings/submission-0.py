class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        start = 0

        for i in range(n):
            for j in range(2):
                low = i
                high = i+j

                while low >=0 and high < n and s[low]  == s[high]:
                    count += 1
                    low -= 1
                    high += 1   

        return count
        