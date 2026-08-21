class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def validate(freq): # check all required chars are found
            for x in freq.keys():
                if freq[x] > 0:
                    return False
            return True
        freq = {}
        l = 0
        res = ""
        for i in range(len(t)): # construct the required chars
            freq[t[i]] = freq.setdefault(t[i], 0) + 1
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]]-=1
            while validate(freq):
                if len(res)>(r-l+1) or res=="":
                    res = s[l:r+1]
                if s[l] in freq:
                    freq[s[l]]+=1
                l+=1
        return res