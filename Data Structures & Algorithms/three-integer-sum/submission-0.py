class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        map = {}
        valid = set()
        for i, x in enumerate(nums):
            map[x] = i
        for i, x in enumerate(nums):
            for j in range(i+1, len(nums)):
                if map.get(-nums[j]-x, -1)>j:
                    arr = [x, nums[j], -nums[j]-x]
                    arr.sort()
                    valid.add(tuple(arr))
        
        return [list(i) for i in valid]