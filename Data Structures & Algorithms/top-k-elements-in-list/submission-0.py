class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        freq = sorted(freq.items(), key = lambda item: item[1], reverse=True)
        for i in freq:
            result.append(i[0])
        
        return result[0:k]


        