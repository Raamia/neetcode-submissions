import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        sol = []
        for i in count:
            heap.append([count[i],i])
        heapq.heapify_max(heap)
        for i in range(k):
            sol.append(heapq.heappop_max(heap)[1])
        return sol