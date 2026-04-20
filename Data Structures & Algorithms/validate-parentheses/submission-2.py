class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {"]":"[", "}":"{", ")":"("}
        for i in s:
            if i in "[{(":
                stack.append(i)
            elif i in "]})":
                if not stack:
                    return False
                temp = stack.pop()
                if lookup[i] != temp:
                    return False
        return not stack