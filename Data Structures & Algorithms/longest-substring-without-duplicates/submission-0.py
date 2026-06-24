class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        seq = set()
        seq_len = 0


        for r in range(len(s)):
            while s[r]  in seq:
                seq.remove(s[l])
                l += 1
            seq.add(s[r])
            seq_len = max(seq_len, r-l+1)
        return seq_len
        
            