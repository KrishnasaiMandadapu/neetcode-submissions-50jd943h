class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        
        hashMap={'}':'{',')':'(',']':'['}
        for i in range(len(s)):
            
            if s[i] in hashMap:
                if stack and s[i] and stack[-1]==hashMap[s[i]]:
                        stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if stack:
            return(False)
        else:
            return(True)






