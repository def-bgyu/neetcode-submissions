class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = dict()
        seen2 = dict()

        for i in s:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        
        for j in t:
            if j not in seen2:
                seen2[j] = 1
            else:
                seen2[j] += 1

        if seen == seen2:
            return True

        return False
            
        