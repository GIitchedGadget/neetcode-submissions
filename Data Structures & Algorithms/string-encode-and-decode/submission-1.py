class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += str(len(i)) + "#" + i
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        p1 = 0
        p2 = 0
        result = []
        while p1 < len(s):
            while s[p2] != "#":
                p2 += 1
            print(s[p1:p2])
            skip = int(s[p1:p2])
            p1 = p2 + 1
            p2 += skip + 1
            result.append(s[p1:p2])
            p1 = p2
        return result



