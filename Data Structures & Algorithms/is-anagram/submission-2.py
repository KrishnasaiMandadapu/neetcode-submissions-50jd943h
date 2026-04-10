class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (set(s)==set(t) and (len(s)==len(t))):
            for char in set(s):
                if s.count(char)!=t.count(char):
                    return False
            return True
        else:
            return False
    