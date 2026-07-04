class Solution:
    def trap(self, height: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(height) - 1
        leftMax, rightMax = height[ptr1], height[ptr2]
        result = 0
        while ptr1 < ptr2:
            if leftMax < rightMax:
                ptr1 += 1
                leftMax = max(leftMax, height[ptr1])
                result += leftMax - height[ptr1]
            else:
                ptr2 -= 1
                rightMax = max(rightMax, height[ptr2])
                result += rightMax - height[ptr2]
        return result

