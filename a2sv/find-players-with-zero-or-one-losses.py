class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        score = defaultdict(list)
        for match in matches:
            score[match[0]].append(1)
            score[match[1]] .append(-1)
        none =[]
        one = []
        for s in score:
            if score[s].count(-1) == 0:
                none.append(s)
            elif score[s].count(-1) == 1:
                one.append(s)
        return [sorted(none),sorted(one)]