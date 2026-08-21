class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        l = 0
        shortest = len(s)+1
        res = (0, -1)
        count = len(t)
        for i in range(len(t)):
            freq[t[i]] = freq.setdefault(t[i], 0) + 1
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]]-=1
                if freq[s[r]]>=0:
                    count-=1
            while count<1:
                if shortest > (r-l+1):
                    res = (l, r)
                    shortest = (r-l+1)
                if s[l] in freq:
                    freq[s[l]]+=1
                    if freq[s[l]]>0:
                        count+=1
                l+=1
        return s[res[0] : res[1]+1]