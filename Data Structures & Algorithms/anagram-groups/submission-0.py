from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        groups = {}

        for i in strs:
            cleaned = "".join(sorted(i))
            groups[cleaned] = groups.get(cleaned, []) + [i]

        for i in groups:
            result.append(groups.get(i))
            
        return result

        

        