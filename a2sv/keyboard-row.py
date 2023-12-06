class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1= {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
        r2 = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
        r3 = {"z", "x", "c", "v", "b", "n", "m"}
        ans  =[]
        for word in words:
            s ={i.lower() for i in word}
            if s.issubset(r1) or s.issubset(r2) or s.issubset(r3):
                ans.append(word)
        return ans