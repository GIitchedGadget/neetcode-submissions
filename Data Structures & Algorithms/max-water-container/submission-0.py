class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1, p2 = 0, len(heights) - 1
        maxArea = 0
        while p1 < p2:
            s = self.getArea(heights, p1, p2)
            if s > maxArea:
                maxArea = s
            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1

        return maxArea



    
    def getArea(self, heights, p1, p2) -> int:
        #where p1 and p2 are INDICES

        height = min(heights[p1], heights[p2])
        length = p2 - p1
        return height * length
