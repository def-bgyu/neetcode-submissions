class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = []
        stack = []

        for i in range(len(temperatures)):
            result.append(0)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] =  i - prev_day
            stack.append(i)

        return result