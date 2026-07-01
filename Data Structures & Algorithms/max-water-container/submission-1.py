class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        maxArea = 0
        while p1 < p2:
            area = self.getArea(heights[p1], heights[p2], p2 - p1)
            if (area > maxArea):
                maxArea = area
            if heights[p1] == heights[p2]:
                p1 += 1
                p2 -= 1
            elif heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1
        return maxArea


    def getArea(self, p1: int, p2: int, distance: int) -> int:
        return min(p1, p2) * distance