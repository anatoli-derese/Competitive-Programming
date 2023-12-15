class OrderedStream:

    def __init__(self, n: int):
        self.len = n
        self.dict = defaultdict(str)
        self.begin = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        ans =[]
        self.dict[idKey] = value
        if idKey == self.begin:
            while self.dict[idKey] : 
                ans.append(self.dict[idKey])
                idKey +=1
                self.begin +=1
        return ans  
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)