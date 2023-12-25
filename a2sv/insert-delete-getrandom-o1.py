class RandomizedSet:

    def __init__(self):
        self.hash_index = {}
        self.random =[]

    def insert(self, val: int) -> bool:
        if val in self.hash_index:
            return False
        self.random.append(val)
        self.hash_index[val] = len(self.random) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.hash_index:
            rem_index = self.hash_index[val]
            last_elem = self.random[-1]
            self.random[rem_index] = last_elem
            self.random[-1] = val
            self.random.pop()
            self.hash_index[last_elem] = rem_index
            rem_index = self.hash_index.pop(val)
            return True
        return False 

    def getRandom(self) -> int:
        return random.choice(self.random)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()