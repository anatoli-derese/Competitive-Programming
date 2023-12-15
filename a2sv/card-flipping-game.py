class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        anti_set = set()
        ans = float('inf')
        fr = set(fronts)
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                anti_set.add(fronts[i])
        for i in range(len(fronts)):
            if fronts[i] not in anti_set and backs[i] not in anti_set:
                ans = min(min(backs[i], fronts[i]) , ans)
            elif fronts[i] not in anti_set:
                ans = min(fronts[i], ans)
            elif backs[i] not in anti_set:
                ans = min(backs[i], ans)
        return 0 if ans == float('inf') else ans

        