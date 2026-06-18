class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = "" 
        for word in strs:
            encoded_string += str(len(word)) + '#' + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs =[]
        i = 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            word = s[j+1:j+length+1]
            i = j+ length+ 1
            decoded_strs.append(word)
        return decoded_strs
