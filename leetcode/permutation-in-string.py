class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        compArr =[0] * 26
        windArr = [0] * 26
        for i in range(len(s1)):
            compArr[
                ord(s1[i]) - ord("a")
            ] +=1
            windArr [
                ord(s2[i]) - ord("a")
            ] +=1
        if compArr == windArr:
            return True
        i, j = 1, len(s1)
        while j < len(s2):
            windArr[ord(s2[i-1])- ord('a')] -=1
            windArr[ord(s2[j]) - ord('a')] +=1
            if compArr == windArr:
                return True
            i +=1
            j +=1
        return False

        
        
        