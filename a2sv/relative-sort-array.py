class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        ans = []
        set_arr = set(arr2)
        for num in arr2:
            for _ in range(count[num]):
                ans.append(num)
        for num in sorted(arr1):
            if num not in set_arr:
                ans.append(num)
        return ans