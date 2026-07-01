class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        maxLength = 0
        dupes = set()
        while p2 != len(s):
            length = 0
            if s[p2] in dupes:
                dupes.remove(s[p1])
                p1 += 1
                continue
            else:
                dupes.add(s[p2])
                p2 += 1
            length = p2 - p1
            if length > maxLength:
                maxLength = length
        return maxLength       
