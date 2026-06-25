class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            l = 0
            s1_freq = {}
            window_freq = {}

            for i in (s1):
                s1_freq[i] = s1_freq.get(i, 0) + 1
            

            for r in range(len(s2)):
                window_freq[s2[r]] = window_freq.get(s2[r], 0) +1


                if (r-l +1) == len(s1):
                    if s1_freq == window_freq:
                        return True

                    window_freq[s2[l]] -= 1
                    if window_freq[s2[l]] == 0:
                        del window_freq[s2[l]]
                    l += 1

            return False


            
