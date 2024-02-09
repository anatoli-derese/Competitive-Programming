class Solution:
    def bestClosingTime(self, customers: str) -> int:
        nctr, yctr = 0,0
        nc =[0]
        yc =[]
        for i in range(len(customers)):
            if customers[i] == "N":
                nctr +=1
            if customers[~i] =="Y":
                yctr +=1
            nc.append(nctr)
            yc.append(yctr)
        yc.reverse()
        yc.append(0)
        temp = float('inf')
        for i in range(len(yc)-1, -1, -1):
            if yc[i] + nc[i] <= temp:
                temp = yc[i] + nc[i]
                ans = i 
        return ans