class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        absmax = 0
        for i in nums:
            if i-1 in seen:
                continue
            else:
                localmax = 1
                it = 1
                while True:
                    if i+it in seen:
                        localmax+=1
                        it+=1
                    else:
                        break
                absmax = max(absmax, localmax)
        return absmax