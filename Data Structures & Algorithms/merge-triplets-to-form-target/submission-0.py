class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        pos = []
        for i in triplets:
            if i[0] <= target[0] and i[1] <= target[1] and i[2] <= target[2]:
                pos.append(i)
        if len(pos) == 0:
            return False
        sol1 = False
        sol2 = False
        sol3 = False
        for i in pos:
            if i[0] == target[0]:
                sol1 = True
            if i[1] == target[1]:
                sol2 = True
            if i[2] == target[2]:
                sol3 = True
        return sol1 and sol2 and sol3

            