class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orders = {order[i]:i for i in range(len(order))}
        matrix =[]
        for word in words:
            temp =[]
            for c in word:
                temp.append(orders[c])
            matrix.append(temp)
        t = sorted(matrix)
        return t == matrix