class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # Do sliding widndow for false
        tc = 0
        left = 0
        fans = -1
        for right in range(len(answerKey)):
            if answerKey[right] == "T":
                tc +=1
            while tc > k and left < len(answerKey):
                if answerKey[left] == "T":
                    tc -=1
                left +=1
            fans = max(fans, right-left +1)
        # Do for True "T T F T T T T T F T"
        fc = 0
        left = 0
        tans = -1
        for right in range(len(answerKey)):
            if answerKey[right] == "F":
                fc +=1
            while fc > k and left < len(answerKey):
                if answerKey[left] == "F":
                    fc -=1
                left +=1
            tans = max(tans, right-left +1)
        return max(tans,fans)


        