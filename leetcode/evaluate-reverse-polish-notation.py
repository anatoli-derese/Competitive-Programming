class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for exp in tokens:
            if exp in "+-*/":
                ans = eval(stack[-2] + exp + stack[-1])
                stack.pop()
                stack.pop()
                if ans >= 0:
                    ans = math.floor(ans)
                else:
                    ans = math.ceil(ans)
                stack.append(str(ans))
            else:
                stack.append(str(exp))
        return int(stack[0])
