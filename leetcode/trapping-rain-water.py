class Solution:
    def trap(self, height: List[int]) -> int:
        maxAfter = [-1] * len(height)
        maxBefore = [-1] * len(height)
        
        mono_stack = []
        for i in range(len(height)):
            while len(mono_stack)>0 and height[mono_stack[-1]] < height[i]:
                new = mono_stack.pop()
                maxAfter[new] = i
            mono_stack.append(i)
        
        mono_stack = []
        for i in range(len(height)-1, -1, -1):
            while len(mono_stack)>0 and height[mono_stack[-1]] < height[i]:
                new = mono_stack.pop()
                maxBefore[new] = i
            mono_stack.append(i)
        
        
        res = 0
        tracker = defaultdict(list)
        for k in range(len(height)):
            if maxBefore[k] == -1 or maxAfter[k] == -1 or ([maxBefore[k], maxAfter[k]] == tracker[height[k]]):
                continue
            tracker[height[k]] = [maxBefore[k], maxAfter[k]]
            x = min(height[maxBefore[k]], height[maxAfter[k]])
            dif = maxAfter[k] - maxBefore[k] - 1
            res += (dif*(x-height[k]))
        
        return res
