class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        near_ghost = float('inf')
        for ghost in ghosts:
            dist = abs(ghost[0]- target[0]) + abs(ghost[1]- target[1])
            near_ghost = min(dist,near_ghost)
        player = abs(target[0]) + abs(target[1])
        return player < near_ghost