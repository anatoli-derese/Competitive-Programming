class Solution:
    def __init__(self):
        self.i = 0


    def decodeString (self, s: str) -> str:

        r = ""
        while self.i < len(s) and s[self.i]!= "]":
            if s[self.i].isdigit():
                k = ""
                while s[self.i].isdigit():
                    k += s[self.i]
                    self.i +=1
                k = int(k)
                print(k)
                self.i +=1
                temp = self.decodeString(s)
                r += temp*k
                self.i +=1
            else:
                r += s[self.i]
                self.i +=1
        return r
    # return decodeString(s)


# class Solution:
#     def __init__(self):
#         self.self.i = 0

#     def decodeString(self, s: str) -> str:
#         result = []
#         while self.self.i < len(s) and s[self.self.i] != ']':
#             if s[self.self.i].isdigit():
#                 k = 0
#                 while self.self.i < len(s) and s[self.self.i].isdigit():
#                     k = k * 10 + int(s[self.self.i])
#                     self.self.i += 1
#                 self.self.i += 1
#                 r = self.decodeString(s)
#                 result.append(r * k)
#                 self.self.i += 1
#             else:
#                 result.append(s[self.self.i])
#                 self.self.i += 1
#         return ''.join(result)
