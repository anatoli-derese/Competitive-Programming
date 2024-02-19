class Solution:
    def simplifyPath(self, path: str) -> str:
        devided = path.split("/")
        path = []
        print(devided)
        for dir in devided:
            if  dir =="..":
                if len(path) > 0:
                    path.pop()
            elif dir != "" and dir != ".":
                path.append(dir)
        return "/" + "/".join(path)