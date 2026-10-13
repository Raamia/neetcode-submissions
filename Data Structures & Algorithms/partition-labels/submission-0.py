class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = {}
        sol = []
        for i in range(len(s)):
            map[s[i]] = i
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, map[s[i]])
            if i == end:
                sol.append(end-start+1)
                start = end+1
                end = 0
        return sol
