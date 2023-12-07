class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        length = right + 1
        line = [0] * length 
        for r in ranges:
            if r[0] < length:
                line[r[0]] +=1
            if r[1]+1 < length:
                line[r[1]+1] -=1
        pre = [0]*len(line)
        for i in range(len(line)):
            if i != 0:
                pre[i] = pre[i-1] + line[i]
            else:
                pre[i] = line[i]
        for i in range(left,right+1):
            if pre[i] == 0:
                return False
        return True