class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i , num in enumerate(tickets):
            if i <= k:
                if num < tickets[k]:
                    ans += num
                else:
                    ans += tickets[k]
            else:
                if num <= tickets[k]-1:
                    ans += num
                else:
                    ans += tickets[k] -1
        return ans

                
            

        