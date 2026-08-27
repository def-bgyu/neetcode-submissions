class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        if not stones:
            return 0

        while len(stones) >1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x<y:
                heapq.heappush(stones,x-y)
            elif x>y:
                heapq.heappush(stones,y-x)
        return -stones[0] if stones else 0