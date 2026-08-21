class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if nums[r] > nums[l]:
            return nums[l]
        m = (r-l)//2+l
        while m>l:
            if nums[m] > nums[l]:
                l=m
            else:
                r=m
            m = (r-l)//2+l
        if nums[m]-nums[l] == m-l:
            return nums[r]
        return nums[m]