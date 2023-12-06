class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        indexes_of_one = []
        for i, state in enumerate(boxes):
            if state == "1":
                indexes_of_one.append(i)
        ans =[]
        for i in range(len(boxes)):
            temp = 0
            for num in indexes_of_one:
                temp += abs(num - i)
            ans.append(temp)
        return ans

        