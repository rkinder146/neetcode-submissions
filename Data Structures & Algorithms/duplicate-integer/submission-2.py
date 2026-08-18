class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = set()
        for x in nums:
            if map.__contains__(x):
                return True
            map.add(x)
        return False
        