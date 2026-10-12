class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxv = -1
        for i in range(len(arr)-1, -1 ,-1):
            temp = arr[i]
            arr[i] = maxv
            maxv = max(maxv, temp)
        return arr