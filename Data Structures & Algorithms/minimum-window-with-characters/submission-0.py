class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = {}
        sDict = {}
        for c in t:
            tDict[c] = tDict.get(c, 0) + 1
        need = len(tDict)
        have = 0
        ptr1 = 0
        shortestString = ""
        for ptr2 in range(len(s)):
            if s[ptr2] in tDict:
                sDict[s[ptr2]] = sDict.get(s[ptr2], 0) + 1
                if sDict[s[ptr2]] == tDict[s[ptr2]]:
                    have += 1
            while have == need:
                if shortestString == "" or (ptr2 - ptr1 + 1) < len(shortestString):
                    shortestString = s[ptr1:ptr2 + 1]
                if s[ptr1] in tDict:
                    sDict[s[ptr1]] -= 1
                    if sDict[s[ptr1]] < tDict[s[ptr1]]:
                        have -= 1
                ptr1 += 1
        return shortestString