class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for x in strs:
            key = sorted(x)
            key = "".join(key)
            group.setdefault(key,[]).append(x)
        return list(group.values())