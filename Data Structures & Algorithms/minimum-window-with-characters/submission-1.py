class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        l = 0
        res = ""
        count = len(t)
        for i in range(len(t)):
            freq[t[i]] = freq.setdefault(t[i], 0) + 1
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]]-=1
                if freq[s[r]]>=0:
                    count-=1
            while count<1:
                if len(res)>(r-l+1) or res=="":
                    res = s[l:r+1]
                if s[l] in freq:
                    freq[s[l]]+=1
                    if freq[s[l]]>0:
                        count+=1
                l+=1
        return res