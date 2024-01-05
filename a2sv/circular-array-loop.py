class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        checked = set()
        for i in range(len(nums)):
            visited = set()
            if i not in checked:
                while True:
                    if i in visited: return True
                    if i in checked: 
                        break
                    visited.add(i)
                    checked.add(i)
                    prev = i
                    i = (i + nums[i]) % len(nums)
                    if prev == i:
                        break
                    if (nums[i] >0) != (nums[prev] >0):
                        break
        return False