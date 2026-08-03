class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        hashmap={len(s):True}
        def dfs(i):

            # if i==len(s):
            #     return True
            if i in hashmap:
                return hashmap[i]

            for w in wordDict:

                if ((i+len(w)<=len(s))and (s[i:i+len(w)]==w)):

                    if dfs(i+len(w)):
                        hashmap[i]=True
                        return True

            hashmap[i]=False
            return False

        return dfs(0)