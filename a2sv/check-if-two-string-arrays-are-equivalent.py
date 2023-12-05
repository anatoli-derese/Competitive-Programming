class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first = "".join(word1)# concatenate the first word
        second = "".join(word2) # concatenate the second word
        return first == second
        