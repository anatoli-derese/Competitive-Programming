class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count  = {}
        ans = 0
        for answer in answers:
            if answer == 0:
                ans +=1
            elif answer not in count  :
                count[answer] = 1
                ans += answer + 1
            else:
                count[answer ] += 1
                if count[answer] > answer:
                    del count[answer]
        return ans
                