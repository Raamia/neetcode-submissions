class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        sol = []
        for i in strs:
            if "".join(sorted(i)) in map:
                sol[map["".join(sorted(i))]].append(i)
            else:
                map["".join(sorted(i))] = len(sol)
                sol.append([i])
        return sol