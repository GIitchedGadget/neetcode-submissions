import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = []
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for number, frequency in freq.items():
            heapq.heappush(heap, (frequency, number))
            if len(heap) > k:
                heapq.heappop(heap)
        
        for tuple in heap:
            result.append(tuple[1])

        return result
        



        