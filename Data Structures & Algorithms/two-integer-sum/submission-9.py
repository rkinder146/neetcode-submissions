class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, x in enumerate(nums):
            j = map.get(target-x)
            if j is not None:
                return [j, i]
            map[x] = i
        return []