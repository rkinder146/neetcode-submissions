class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        zeroCount = 0
        for x in nums:
            if (x!=0):
                mult *= x
            else:
                zeroCount+=1
        return [0 if zeroCount>1 or (zeroCount==1 and x!=0) else int(mult/(1 if x==0 else x)) for x in nums]

        