class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        l_max = height[0]
        r_max = height[len(height) - 1]
        count = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    count += l_max - height[l]
                l += 1
            if height[l] >= height[r]:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    count += r_max - height[r]
                r -= 1
        return count