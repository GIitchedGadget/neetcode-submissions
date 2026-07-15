class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += str(len(i)) + "#" + i
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        result = []
        ptr1 = 0
        ptr2 = 0
        while ptr2 < len(s):
            while s[ptr2] != "#":
                ptr2 += 1
            length = int(s[ptr1:ptr2])
            ptr1 = ptr2 + 1
            ptr2 += length + 1
            result.append(s[ptr1:ptr2])
            ptr1 = ptr2
        
        return result
            
