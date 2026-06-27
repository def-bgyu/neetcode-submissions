class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq= {}
        window_freq ={}
        minLength = float("infinity")
        l=0
        have = 0
        result = ""
        

        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
        
        need = len(t_freq)

        for r in range(len(s)):
            window_freq[s[r]] = window_freq.get(s[r], 0) +1

            if s[r] in t_freq and window_freq[s[r]] == t_freq[s[r]]:
                have += 1

            while have == need:
                if (r-l +1) < minLength:
                    minLength = r-l +1
                    result = s[l:r+1]

                window_freq[s[l]] -= 1

                if s[l] in t_freq and window_freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1
        
        return result
        

        
        