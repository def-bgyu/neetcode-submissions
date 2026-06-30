class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        op = ["+", "-", "/", "*"]
        result = 0

        for i in tokens:
            if i in op:
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    result = a + b
                elif i == "-":
                    result = a - b
                elif i == "*":
                    result = a * b
                elif i == "/":
                    result = int(a/b)

                stack.append(result)

            else:
                num = int(i)
                stack.append(num)
            
        return stack[-1]

        