class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        q = deque([deck[0]])
        for i in range(1, len(deck)):
            back = q.pop()
            q.appendleft(back)
            q.appendleft(deck[i])
        return q