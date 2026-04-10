class Solution:
    def isPalindrome(self, s: str) -> bool:
        array=s.split()
        newString=''.join(array)
        filteredString="".join(c.lower() for c in newString if c.isalnum())
        filteredString
        if len(filteredString)==0:
            return True
        r=0
        l=len(filteredString)-1
        if l%2==0:
            i=0
        else:
            i=1
        while(r<=l//2+i):
            if filteredString[r]!=filteredString[l]:
                return False
                break
            r+=1
            l-=1
            
        else:
            return True