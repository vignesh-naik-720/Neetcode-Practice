class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        l_max = height[0]
        r_max = height[len(height) - 1]
        count = 0
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(height[l], l_max)
                count += l_max - height[l]
            else:
                r -= 1
                r_max = max(height[r], r_max)
                count += r_max - height[r]
        return count