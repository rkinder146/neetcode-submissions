class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:return False
        stack = []
        m = {"(":")","[":"]", "{":"}"}
        for x in s:
            if x in m:
                stack.append(x)
            else:
                if len(stack) == 0 or x != m[stack.pop()]:
                    return False
        return len(stack) == 0
            
