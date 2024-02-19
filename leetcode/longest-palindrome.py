class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        values = sorted(freq.values(), reverse = True)
        ans, flag = 0 , False
        for num in values:
            if num % 2 == 1 and not flag:
                ans += num
                flag = True
            elif num % 2 == 0:
                ans += num
            else:
                ans += num - 1
        return ans
        