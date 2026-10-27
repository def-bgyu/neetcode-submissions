class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Anagram -> list
        #sort all string and add them to a dict, values will return the freq of all anagrams.
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())