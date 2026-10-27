class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_freq[i][0])
            
        return res
