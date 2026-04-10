from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp=defaultdict(list)
        for String in strs:
            Sstring="".join(sorted(String))
            temp[Sstring].append(String)
        return list(temp.values())