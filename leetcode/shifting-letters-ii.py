class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shiftArr = [0 for _ in range(len(s)+1)]
        for arr in shifts:
            if arr[-1]:
                shiftArr[arr[0]] += 1
                shiftArr[arr[1]+1] -=1
            else:
                shiftArr[arr[0]] -=1
                shiftArr[arr[1]+1] +=1
        res =""
        for i in range(len(s)):
            if i != 0:
                shiftArr[i] += shiftArr[i-1]
            temp = (ord(s[i]) - 97 + shiftArr[i]) % 26 + 97
            res += chr(temp)
        return res
        