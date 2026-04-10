class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1,temp2=set(s),set(t)
        if (temp1==temp2 and (len(s)==len(t))):
            for char in temp1:
                if s.count(char)!=t.count(char):
                    return False
            return True
        else:
            return False
    