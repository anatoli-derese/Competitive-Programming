class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        maximum , indx = -1,0
        for i, num in enumerate(arr):
            if num == maximum: return False
            if num > maximum:
                maximum = num
                indx = i
        if indx == 0 or indx == len(arr) -1:
            return False
        i, j = 0,1
        while j < indx:
            if arr[j] <= arr[i]:
                return False
            i +=1
            j +=1
        i += 2
        j += 2
        while j < len(arr):
            if arr[j] >= arr[i]:
                return False
            i +=1
            j +=1
        return True


        