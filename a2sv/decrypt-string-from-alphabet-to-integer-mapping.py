class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        nums =[]
        d ={}
        for i in range(1,27):
            d[i] = chr(97+i-1)
        for i in s:
            if i =="#":
                temp = stack.pop() + stack.pop()
                stack.append(temp[::-1])
            else:
                stack.append(i)
        ans =""
        for i in stack:
            ans += d[int(i)]
        return ans