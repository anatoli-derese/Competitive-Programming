class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexes = {nums2[i] : i for i in range(len(nums2))}
        stack = []
        ans = [0] * len(nums2)
        for i in range(len(nums2)-1, -1, -1):
            while len(stack) > 0 and stack[-1] <= nums2[i]:
                stack.pop()
            if len(stack) == 0:
                ans[i] = -1
            else:
                ans[i] = stack[-1]
            stack.append(nums2[i])
        return [ans[indexes[num]] for num in nums1]
