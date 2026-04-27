class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

# nums = [3,4,5,6,1,2]
# res = nums[0] = 3, l = 0, r = len(nums) - 1 = 5
# WLOOP
# is l <= r <-- 0 <= 5 <-- True
# if nums[l] < nums[r] <-- False
# m = (l+r)//2 <-- m = 2
# res = min(res, nums[2]) <-- res = 3
# if nums[2] >= nums[0] <-- True
# l = m+1 <-- l = 3
# is l <= r ? <-- 3 <= 5 <-- True
# if nums[3] < nums[5] ? <-- False
# m = (l+r)//2 <-- m = 4
# res = min(3, nums[4]) <-- res = 1
# if nums[4] >= nums[3] <-- false
# r = m - 1 <-- r = 3
# return res = 1
