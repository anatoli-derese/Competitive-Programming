class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d ={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        e ={0:'0',1:'1',2:'2',3:'3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

        n1 , n2 = 0,0
        for c in num1:
            n1 = (10*n1)+ d[c]
        for c in num2:
            n2 = (10*n2) + d[c]
        temp = n1*n2
        print(temp)
        ans = ""
        if temp == 0:
            return "0"
        while temp > 0:
            ans += e[temp %10]
            temp = temp//10
        return ans[::-1]