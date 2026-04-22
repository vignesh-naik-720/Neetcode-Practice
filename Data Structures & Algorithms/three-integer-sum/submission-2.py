class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if sorted_nums[i] > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            l = i+1
            r = len(sorted_nums) - 1
            while l < r:
                three_sum = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([sorted_nums[i],sorted_nums[l],sorted_nums[r]])
                    l += 1
                    r -= 1
                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l += 1
        return result
