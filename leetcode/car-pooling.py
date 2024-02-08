class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        miles = max(trips[i][2] for i in range(len(trips)))
        line = [0] * miles
        for val, start, end in trips:
            line[start] += val
            if end < miles:
                line[end] -= val
        for i in range(1,len(line)):
            line[i] += line[i-1]
        return capacity >= max(line)
        