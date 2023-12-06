class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for num in nums: #differenciate the positive and the negatives
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        ans = []
        i = 0
        while i < len(pos): # put them on the anwer variable
            ans.append(pos[i])
            ans.append(neg[i])
            i+=1
        return ans