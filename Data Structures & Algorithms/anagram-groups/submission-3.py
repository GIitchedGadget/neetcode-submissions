class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        result = []
        for i in strs:
            raw = "".join(sorted(i))
            groups[raw] = groups.get(raw, []) + [i]

        for i in groups:
            result.append(groups[i])

        return result
        