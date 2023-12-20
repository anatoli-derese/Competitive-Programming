class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp =""
        for num in digits:
            temp += str(num)
        temp = str(int(temp) + 1)
        ans  = [int(i) for i in temp]
        return ans
        
        