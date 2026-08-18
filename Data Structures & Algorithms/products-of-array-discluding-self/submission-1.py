class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd = [1]*len(nums)
        sufProd = [1]*len(nums)
        for i in range(1, len(nums)):
            preProd[i] = preProd[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            sufProd[i] = sufProd[i+1]*nums[i+1]
        return [preProd[i] * sufProd[i] for i in range(len(nums))]