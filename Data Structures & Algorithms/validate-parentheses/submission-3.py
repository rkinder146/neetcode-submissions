from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        map = {"(":")","[":"]", "{":"}"}
        for x in s:
            if x in map.keys():
                stack.append(x)
            else:
                if len(stack) == 0 or x != map[stack.pop()]:
                    return False
        return len(stack) == 0
            
