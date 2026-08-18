import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = re.sub(r'[^a-z0-9]', '', s.lower())

        left, right = 0, len(x)-1 
        while (left < right):
            if x[left]!=x[right]:
                return False
            left += 1
            right -= 1
        return True