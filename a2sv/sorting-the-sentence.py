class Solution:
    def sortSentence(self, s: str) -> str:
        temp = s.split(" ")[::]
        positions =[int(i[-1]) for i in temp]
        ans = []
        for i in range(len(positions)):
            index = positions.index(i+1)
            string = temp[index][:-1]
            ans.append(string)
        stringAns =""
        for x in ans:
            stringAns += x + " "
        return stringAns.strip()
            