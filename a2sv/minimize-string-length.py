class Solution:
    def minimizedStringLength(self, s: str) -> int:
        count = Counter(s)
        return len(count)
        