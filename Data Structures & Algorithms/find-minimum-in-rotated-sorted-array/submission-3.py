class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        
        while left < right:
            middle = (right-left)//2+left
            if nums[middle]>nums[right]:
                left = middle+1
            else:
                right = middle
        return nums[right]