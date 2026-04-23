class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
                
            curr = prices[r] - prices[l]
            res = max(curr,res)
            
        return res
# p = [10,1,5,6,7,1]
# l = 0
# res = 0
# LOOP
# r = 1
# p[1] < p[0] ? <-- true, hence l = r = 1
# curr = 0, res = 0
# r = 2
# p[2] < p[1] ? <--false
# curr = 5 - 1 = 4, res = 4
# r = 3
# p[3] < p[1] ? <-- false
# curr = 5, res = 5
# r = 4
# p[4] < p[1] ? <--false
# curr = 6, res = 6
# r = 5
# p[5] < p[1] ? <-- false
# curr = 0, res = 6
# LOOP OVER
# return res = 6