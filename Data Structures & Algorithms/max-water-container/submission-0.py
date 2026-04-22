class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #definitions
        l = 0
        r = len(heights) - 1
        l_max = heights[0]
        r_max = heights[len(heights) - 1]
        max_area = 0
        while l < r:
            area = abs(l-r) * min(heights[l], heights[r])
            if area > max_area:
                max_area = area
            else:
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
        return max_area