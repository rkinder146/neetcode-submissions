class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        starts = set()
        for x in nums:
            if x-1 not in seen:
                starts.add(x)
        longest = 0
        for x in starts:
            i = x
            while(i in seen):
                i+=1
            if longest < i-x:
                longest = i-x
        return longest
