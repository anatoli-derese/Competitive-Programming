# Problem: B - String Fusion - https://codeforces.com/gym/526229/problem/B

from collections import defaultdict
tot = 0
class TrieNode:
    def __init__(self) -> None:
        self.children = [None for _ in range(26)]
        self.freq = 0
        self.is_end = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()    
    def add(self,word):
        curr = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if not curr.children[ind]:
                curr.children[ind] = TrieNode()
            curr = curr.children[ind]
            curr.freq +=1
    def deduct(self, word):
        curr = self.root
        tot = 0
        for c in word:
            ind = ord(c) - ord('a')
            if curr.children[ind]:
                curr = curr.children[ind]
                freq = curr.freq
                tot -= 2*freq
            else:
                return tot
        return tot   

words =[]
trie = Trie()
n = int(input())
for _ in range(n):
    word = input()
    trie.add(word)
    tot += len(word)
    words.append(word)

tot = tot*2*n

for w in words:
    tot += trie.deduct(w[::-1])
print(tot)




