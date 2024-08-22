# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        temp = defaultdict(list)
        print(temp)
        for i,s in enumerate(strs):
            a = sorted(s)
            t = "".join(a)
            temp[t].append(i)
        ans =[]
        for i in temp.values():
            h =[]
            for x in i:
                h.append(strs[x])
            ans.append(h)
        return ans