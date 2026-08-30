class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-(x) for x in nums]
        heapq.heapify(maxHeap)

        res = []

        for x in range(k):
            num = heapq.heappop(maxHeap)

        return -num