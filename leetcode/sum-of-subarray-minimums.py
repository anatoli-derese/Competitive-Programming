class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        pref = [1]* len(arr)
        suff = [1] * len(arr)
        stack = []
        for i,num in enumerate(arr):
            temp = 1
            while len(stack) > 0 and stack[-1][0] >= num:
                temp += stack.pop()[1]
            stack.append((num, temp))
            pref[i] = temp
        stack = []
        for i in range(len(arr)-1, -1, -1):
            temp = 1
            while len(stack) > 0 and stack[-1][0] > arr[i]:
                temp += stack.pop()[1]
            stack.append((arr[i], temp))
            suff[i] = temp 
        ans = 0
        for i in range(len(pref)):
            ans += pref[i] * suff[i] * arr[i]
        return ans % ((10**9)+7)
                



        