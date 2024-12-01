class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap: list[int] = []        

        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            else:
                if x > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, x)

        return heap[0]
