# Brute Force
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0

        for i in range(n):
            height = heights[i]

            rightMost = i + 1
            while rightMost < n and heights[rightMost] >= height:
                rightMost += 1

            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1

            rightMost -= 1
            leftMost += 1
            maxArea = max(maxArea, height * (rightMost - leftMost + 1))
        return maxArea

# Optimal
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea