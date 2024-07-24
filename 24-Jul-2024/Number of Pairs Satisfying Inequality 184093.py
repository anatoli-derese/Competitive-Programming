# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        arr = []
        for i in range(len(nums1)):
            arr.append(nums1[i] - nums2[i])


        def devide(l,r):
            if l == r:
                return [arr[l]]
            m = (l+r)//2
            left = devide(l,m)
            right = devide(m+1, r)
            return merge(left, right)
        ans = 0
        def merge(left, right):
            nonlocal ans
            i,j = 0,0
            while i < len(left) and j < len(right):
                if left[i] <= right[j] + diff:
                    ans += len(right) - j
                    i += 1
                else:
                    j +=1
            
            i,j = 0,0
            merged = []
            left.append(float('inf'))
            right.append(float('inf'))
            
            while i < len(left)  and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i +=1
                else:
                    merged.append(right[j])
                    j +=1
            merged.pop()
            return merged
        
        devide(0, len(arr)-1)
        
        return ans
