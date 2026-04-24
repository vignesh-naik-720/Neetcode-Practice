class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

# s = "AAABABB", k = 1
# count = {}, res = 0, l = 0, maxf = 0
# LOOP
# r = 0
# count[s[0]] = 1 + count.get(s[0], 0) = 1 <-- count = {"A" : 1}
# maxf = max(0, 1) = 1
# WLOOP
# while (0 - 0 + 1) - 1 > 1 <-- false
# WCLOSE
# res = max(0, 0 - 0 + 1) = 1
# r = 1
# count[s[1]] = 1 + count.get(s[1], 0) = 2 <-- count = {"A" : 2}
# maxf = max(1, 2) = 2
# WLOOP
# while (1 - 0 + 1) - 2 > 1 <-- false
# WCLOSE
# res = max(1, 1 - 0 + 1) = 2
# r = 2
# count[s[2]] = 1 + count.get(s[2], 0) = 3 <-- count = {"A" : 3}
# maxf = max(2, 3) = 3
# WLOOP
# while (2 - 0 + 1) - 3 > 1 <-- false
# WCLOSE
# res = max(2, 2 - 0 + 1) = 3
# r = 3
# count[s[3]] = 1 + count.get(s[3], 0) = 1 <-- count = {"A" : 3, "B" : 1}
# maxf = max(3, 1) = 3
# WLOOP
# while (3 - 0 + 1) - 3 > 1 <-- false
# WCLOSE
# res = max(3, 3 - 0 + 1) = 4
# r = 4
# count[s[4]] = 1 + count.get(s[4], 0) = 4 <-- count = {"A" : 4, "B" : 1}
# maxf = max(3, 4) = 4
# WLOOP
# while (4 - 0 + 1) - 4 > 1 <-- false
# WCLOSE
# res = max(4, 4 - 0 + 1) = 5
# r = 5
# count[s[5]] = 1 + count.get(s[5], 0) = 2 <-- count = {"A" : 4, "B" : 2}
# maxf = max(4, 2) = 4
# WLOOP
# while (5 - 0 + 1) - 4 > 1 <-- true
#   count[s[0]] = 3 <-- count = {"A" : 3, "B" : 2}
#   l = 1
# while (5 - 1 + 1) - 4 > 1 <-- false
# WCLOSE
# res = max(4, 5 - 1 + 1) = 5
# r = 6
# count[s[6]] = 1 + count.get(s[6], 0) = 3 <-- count = {"A" : 3, "B" : 3}
# maxf = max(4, 3) = 4
# WLOOP
# while (6 - 1 + 1) - 4 > 1 <-- true
#   count[s[1]] = 2 <-- count = {"A" : 2, "B" : 2}
#   l = 2
# while (6 - 2 + 1) - 4 > 1 <-- false
# WCLOSE
# res = max(4, 6 - 2 + 1) = 5

# return res = 5