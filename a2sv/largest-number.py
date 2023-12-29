class Solution:
    def comparator_reverse(self,num1,num2):
        first = str(num1) + str(num2)
        second = str(num2) + str(num1)
        if int(first) > int(second):
            return False
        return True
    def largestNumber(self, num: List[int]) -> str:
        for i in range(len(num)):
            swap = False
            for j in range(0,len(num)-i-1):
                if self.comparator_reverse(num[j], num[j+1]):
                    num[j], num[j+1] = num[j+1] , num[j]
                    swap = True
            if not swap:
                break
        temp = [str(i) for i in num]
        ans  = "".join(temp)
        if int(ans) == 0:
            return "0"
        else:
            return ans
        