import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            c = Counter(s)
            map.setdefault(tuple(c[a] for a in string.ascii_lowercase), []).append(s)
        return list(map.values())