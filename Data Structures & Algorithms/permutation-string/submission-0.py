class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        l = 0
        tempcount = Counter(s2[0:len(s1)])
        if count == tempcount:
                return True
        for r in range(len(s1), len(s2)):
            if s2[r] in tempcount:
                tempcount[s2[r]]+=1
            else:
                tempcount[s2[r]] = 1
            tempcount[s2[l]] -=1
            if tempcount[s2[l]] == 0:
                del tempcount[s2[l]]
            l+=1
            if count == tempcount:
                return True
        return False
            