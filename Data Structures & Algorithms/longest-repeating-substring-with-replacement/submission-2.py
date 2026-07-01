class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p1 = 0
        p2 = 0
        freq = {}
        maxFreq = 0
        maxLength = 0
        while p2 != len(s):
            freq[s[p2]] = freq.get(s[p2], 0) + 1
            if freq[s[p2]] > maxFreq:
                maxFreq = freq[s[p2]]
            p2 += 1
            if (p2 - p1) - maxFreq > k: # if # of (needs to be replaced) exceeds k
                freq[s[p1]] = freq.get(s[p1]) - 1
                p1 += 1
            else:
                maxLength = max(maxLength, p2 - p1)
        return maxLength

        