class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dq = deque(senate)
        direBan, radBan = 0,0 
        dire, rad = dq.count("D"), dq.count("R")
        while True:
            # print(dq)
            now = dq.popleft()
            if now == "R":
                if radBan >= 1:
                    radBan -=1
                    rad -=1
                    continue
                else:
                    if dire == 0:
                        return "Radiant"
                    direBan += 1
                    dq.append(now)
            else:
                if direBan >= 1:
                    dire -=1
                    direBan -=1
                    continue
                else:
                    if rad == 0:
                        return "Dire"
                    radBan += 1
                    dq.append(now)

        