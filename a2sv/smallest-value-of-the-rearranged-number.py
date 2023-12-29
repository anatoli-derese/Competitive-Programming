class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        neg = False
        if num < 0 :
            neg = True
        temp = list(map(int,list(str(abs(num)))))
        if  not neg:
            temp.sort()
            if temp[0] == 0:
                i = 0
                while i < len(temp):
                    if temp[i] != 0:
                        break
                    i +=1
                temp[0] , temp[i] = temp[i] , temp[0]
            ans = 0
            for num in temp:
                ans += num
                ans *= 10
            return ans//10      
        else:
            temp.sort(reverse = True)
            ans = 0
            for num in temp:
                ans += num
                ans *= 10
            return -ans//10 
        