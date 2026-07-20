class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for i in s:
            count[i] = count.get(i, 0) + 1

        for i in t:
            if count.get(i, 0) > 0:
                count[i] -= 1
                if count[i] == 0:
                    del count[i]
            else:
                return False

        print(count)

        if not count:
            return True