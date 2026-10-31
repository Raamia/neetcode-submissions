from heapq import heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjlist = {}
        count = 0
        maxtime = 0
        for i in range(1, n+1):
            adjlist[i] = []
        for s, d, w in times:
            adjlist[s].append((w,d))
        heap = [(0,k)]
        seen = set()
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in seen:
                continue
            count+=1
            seen.add(n1)
            maxtime = w1
            for w2, n2 in adjlist[n1]:
                if not n2 in seen:
                    heappush(heap, (w1+w2, n2))
        if count == n:
            return maxtime
        return -1
