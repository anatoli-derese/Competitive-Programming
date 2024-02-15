class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wig = {5:0, 10:0 , 20:0}
        
        for customer in bills:
            if customer == 5:
                wig[5] +=1
            elif customer == 10:
                if wig[5] == 0:
                    return False
                wig[5] -=1
                wig[10] +=1
            else:
                wig[20] +=1
                if wig[10] == 0:
                    if wig[5] < 3:
                        return False
                    wig[5] -=3
                else:
                    if wig[5] < 1:
                        return False
                    wig[5] -=1
                    wig[10] -=1
        return True
                


                
                
        