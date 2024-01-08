class Solution:
    def intervalIntersection(self, list1: List[List[int]], list2: List[List[int]]) -> List[List[int]]:
        if len(list1) == 0 or len(list2) == 0:
            return []
        result = []
    
        for interval1 in list1:
            idx = 0
            while idx < len(list2):
                if interval1[1] >= list2[idx][0] and interval1[0] <= list2[idx][1]:
                    result.append([max(interval1[0], list2[idx][0]), min(interval1[1], list2[idx][1])])
                idx += 1
        return result
