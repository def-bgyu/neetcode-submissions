class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_dict = {}

        for element in nums:
            if element in count_dict:
                count_dict[element] += 1
            else:
                count_dict[element] = 1
    
        sorted_freq = sorted(count_dict.items(), key = lambda x: x[1], reverse=True )

        return [x[0] for x in sorted_freq[:k]]