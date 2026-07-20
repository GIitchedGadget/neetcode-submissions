class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            groups[sorted_s] = groups.get(sorted_s, []) + [s]

        s = groups.values()
        print(s)
        return list(groups.values())
        