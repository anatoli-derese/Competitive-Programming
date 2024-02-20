class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs ={")":"(", "}":"{", "]":"["}
        for par in s:
            if par in "{([":
                stack.append(par)
            else:
                if len(stack) == 0 or stack.pop() != pairs[par] :
                    print(stack)
                    return False
        return len(stack) == 0
        