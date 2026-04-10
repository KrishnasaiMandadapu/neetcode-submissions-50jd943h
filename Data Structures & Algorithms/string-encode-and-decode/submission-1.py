class Solution:

    def encode(self, strs: List[str]) -> str:
        l=""
        for i in strs:
            l+=str(len(i))+"_"+i

        return l
        
    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
        while(i<len(s)):
            j=i
            while(s[j]!='_'):
                j+=1
            value=int(s[i:j])
            i=j+1
            j=value+i
            l.append(s[i:j])
            i=j
        return l
