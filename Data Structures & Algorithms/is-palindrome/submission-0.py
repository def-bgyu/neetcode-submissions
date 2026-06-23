class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(char.lower() for char in s if char.isalnum())
        ptr1 = 0
        ptr2 = len(s) - 1


        while ptr1 <= ptr2:
            if s[ptr1] == s[ptr2]:
                ptr1 += 1
                ptr2 -= 1
                continue
            else:
                return False
        return True
        