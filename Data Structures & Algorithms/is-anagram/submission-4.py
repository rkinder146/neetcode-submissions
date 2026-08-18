class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        for x in s:
            map[x] = map.get(x, 0) + 1
        for x in t:
            map[x] = map.get(x, 0) - 1
            if map[x] < 0:
                return False
        return True