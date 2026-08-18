class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        valid = []
        for i in range(len(nums)-2):
            if (nums[i]>0):
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while(l<r):
                s = nums[l]+nums[r]+nums[i]
                if (s==0):
                    valid.append([nums[i], nums[l], nums[r]])
                    r-=1
                    while(nums[r] == nums[r+1] and l<r):
                        r-=1
                    l+=1
                    while(nums[l] == nums[l-1] and l<r):
                        l+=1
                if (s>0):
                    r-=1
                    while(nums[r] == nums[r+1] and l<r):
                        r-=1
                if (s<0):
                    l+=1
                    while(nums[l] == nums[l-1] and l<r):
                        l+=1
        return valid
                