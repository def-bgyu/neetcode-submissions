class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set()
        for num in nums:
            if num in seen:
                continue
            else: 
                seen.add(num)
        
        longest = 0
        length = 0
        for num in seen:
            if (num-1) not in seen:
                length = 1
                while (num +length) in seen:
                    length += 1
                
                longest = max(longest, length)
    
        return longest