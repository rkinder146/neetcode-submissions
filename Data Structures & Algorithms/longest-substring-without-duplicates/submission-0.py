class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        freq = {}
        longest = 0
        for r in range(len(s)):
            recent = s[r]
            freq[recent] = freq.setdefault(recent, 0)+1
            if freq[recent]<2:
                longest = max(longest, r-l+1)
            while freq[recent]>1:
                freq[s[l]] = freq.get(s[l])-1
                l+=1
        return longest
