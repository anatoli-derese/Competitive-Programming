class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        temp = defaultdict(int)
        for i , word in enumerate(list1):
            if word in list2:
                temp[word]= i + list2.index(word)
        min_val = min(temp.values())
        ans =[]
        for i in temp:
            if temp[i] == min_val:
                ans.append(i)
        return ans
