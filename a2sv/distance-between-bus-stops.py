class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        d1 = sum(distance[min(start,destination):max(start,destination) ])
        d2 = sum(distance) - d1
        return min(d1,d2)
        