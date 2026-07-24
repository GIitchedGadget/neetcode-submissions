class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        maxArea = 0
        p1 = 0
        p2 = length - 1
        while p1 < p2:
            area = self.getArea(min(heights[p1], heights[p2]), p2 - p1)
            if area > maxArea:
                maxArea = area
            if heights[p1] > heights[p2]:
                p2 -= 1
            elif heights[p1] < heights[p2]:
                p1 += 1
            else:
                p1 += 1
                p2 -= 1

        return maxArea

    def getArea(self, height: int, distance: int) -> int:
        return height * distance 