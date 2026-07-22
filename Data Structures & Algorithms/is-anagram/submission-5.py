class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s) != len(t):
            return False
        
        for i in s:
            count[i] = count.get(i, 0) + 1
        
        for i in t:
            if count.get(i, 0) == 0:
                return False
            count[i] = count.get(i, 0) - 1

        return True