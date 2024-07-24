# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10**9 + 7
        track = {i: [0,0] for i in range(len(instructions))}
        for i , num in enumerate(instructions):
            instructions[i] =[num, i]
        def devide(l,r):
            if l == r:
                return [instructions[l]]
            m = (l+r)//2
            left = devide(l,m)
            right = devide(m+1, r)
            return merge(left, right)
        
        def merge(left, right):
            i,j = len(left)-1, len(right)-1
            while i >=0  and j >=0:
                if left[i][0] <= right[j][0]:
                    track[right[j][1]][1] +=((len(left)-1) - i)
                    j -=1
                else:
                    i -=1
            while j > -1:
                track[right[j][1]][1] += len(left)
                j -=1
            left.append((float('inf'),0))
            right.append((float('inf'),0))
            merged =[]
            i,j = 0,0
            while i < len(left) and j < len(right):
                if left[i][0] < right[j][0]:
                    merged.append(left[i])
                    i+=1
                else:
                    if right[j][0] != float('inf'):
                        track[right[j][1]][0] += i
                    merged.append(right[j])
                    j +=1
            merged.pop()
            return merged
        devide(0, len(instructions)-1)
        ans = 0
        for v in track:
            ans += min(track[v])
        return ans % mod

           