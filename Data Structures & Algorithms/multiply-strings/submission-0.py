class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m , n = len(num1), len(num2)

        result = [0] * (m+n)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):

                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                product = digit1 * digit2

                p1 = i + j
                p2 = i + j + 1
                
                # Sum with the existing carry or value at position p2
                total_sum = product + result[p2]
                
                # Distribute the sum to p1 (carry) and p2 (remainder)
                result[p1] += total_sum // 10
                result[p2] = total_sum % 10


        final_str = "".join(str(digit) for digit in result)
        
        # Remove any leading zeros (e.g., [0, 5, 6] -> "056" -> "56")
        return final_str.lstrip("0")        