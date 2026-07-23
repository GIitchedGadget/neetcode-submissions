import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for i in freq:
            heapq.heappush(result, [freq[i], i])
            if len(result) > k:
                heapq.heappop(result)

        return [i[1] for i in result]

        