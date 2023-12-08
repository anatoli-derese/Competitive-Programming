class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content = defaultdict(list)
        for p in paths:
            files = p.split(" ")
            directory = files[0]
            for file in files[1:]:
                name, c = file.split("(")
                content[c[:-1]].append(directory + "/" +name)
        return [content[i] for i in content if len(content[i]) >1 ]     