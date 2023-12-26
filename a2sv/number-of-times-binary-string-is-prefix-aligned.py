class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        _max = float('-inf')
        count = 0
        for i in range(len(flips)):
            _max = max(_max , flips[i])
            if i+1 == _max:
                count +=1
        return count
        