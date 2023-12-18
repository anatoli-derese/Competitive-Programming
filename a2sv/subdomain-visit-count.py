class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict ={}
        for pair in cpdomains:
            temp = pair.split(" ")
            visit = temp[0]
            domain = temp[1].split(".")
            sbd =""
            for i in range(len(domain)):
                sub =domain[len(domain)-1-i]
                if i == 0:
                    sbd = sub
                else:
                    sbd = sub +"."+ sbd
                if sbd in dict:
                    dict[sbd] += int(visit)
                else:
                    dict[sbd] = int(visit)
        ans =[]
        for key in dict:
            ans.append(str(dict[key]) + " " + key)
        return ans

        