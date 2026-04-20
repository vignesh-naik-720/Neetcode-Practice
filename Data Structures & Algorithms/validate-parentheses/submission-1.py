class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {"]":"[", "}":"{", ")":"("}
        for i in s:
            if i in "[{(":
                stack.append(i)
            elif i in "]})":
                if len(stack) == 0:
                    return False
                else:
                    temp = stack.pop()
                    if lookup[i] != temp:
                        return False
        if len(stack) != 0:
            return False
        return True