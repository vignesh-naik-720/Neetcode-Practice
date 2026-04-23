class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_map = {}
        max_len = 0
        start = 0
        for i in range(len(s)):
            if s[i] in c_map and c_map[s[i]] >= start:
                start = c_map[s[i]] + 1
            c_map[s[i]] = i
            max_len = max(max_len, i-start+1)
        return max_len
            