class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        pointer = k
        while tickets[pointer] != 0:
            if tickets[0] == 0:
                temp = tickets.pop(0)
                tickets.append(temp )
            else:
                temp = tickets.pop(0)
                tickets.append(temp - 1)
                time +=1
                if pointer == 0:
                    pointer = len(tickets)
            pointer -=1
        return time
