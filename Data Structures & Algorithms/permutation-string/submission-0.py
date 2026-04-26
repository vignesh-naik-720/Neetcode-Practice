from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        count_s1 = Counter(s1)
        window_count = Counter(s2[:n1])
        if count_s1 == window_count:
            return True
        for i in range(n1, n2):
            window_count[s2[i]] += 1
            window_count[s2[i-n1]] -= 1
            if window_count[s2[i-n1]] == 0:
                del window_count[s2[i-n1]]
            if count_s1 == window_count:
                return True
        return False

# s1 = "abc", s2 = "lecabee"
# n1 = 3, n2 = 7
# if n1 > n2 ? <-- false
# count_s1 = Counter(s1) <-- count_s1 = Counter({"a":1, "b":1, "c":1})
# window_count = Counter(s2[:n1]) <-- Counter(s2[:3]) <-- window_count = Counter({"l":1, "e":1, "c":1})
# if count_s1 == window_count ? <-- Counter({"a":1, "b":1, "c":1}) == Counter({"l":1, "e":1, "c":1}) <-- False
# i = 3
# window_count[s2[i]] += 1 <-- window_count["a"] += 1 <-- window_count = Counter({"l":1, "e":1, "c":1, "a":1})
# window_count[s2[i-n1]] -= 1 <-- window_count["l"] -= 1 <-- window_count = Counter({"l":0, "e":1, "c":1, "a":1})
# if window_count[s2[i-n1]] == 0 ? window_count["l"] == 0 ? <-- True
# del window_count[s2[i-n1]] <-- del window_count["l"] <-- window_count = Counter({"e":1, "c":1, "a":1})
# if count_s1 == window_count ? <-- Counter({"a":1, "b":1, "c":1}) == Counter({"e":1, "c":1, "a":1}) <-- False