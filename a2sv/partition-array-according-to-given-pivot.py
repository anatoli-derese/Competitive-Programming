class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less =[]
        equal =[]
        great = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else: 
                great.append(num)
        return less + equal + great        