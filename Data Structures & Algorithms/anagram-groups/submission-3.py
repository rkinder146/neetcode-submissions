class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            map.setdefault(str(sorted(s)), []).append(s)
        return list(map.values())