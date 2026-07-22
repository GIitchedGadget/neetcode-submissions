import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        result = []
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        freq = sorted(freq.items(), key= lambda x: x[1], reverse=True)

        for i in range(0, k):
            result.append(freq[i][0])

        return result

        
    
        