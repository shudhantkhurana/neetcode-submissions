class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        if len(s) != len(t):
            return False
        for i in s:
            map_s[i] = map_s.get(i,0) + 1
        for i in t:
            map_t[i] = map_t.get(i,0) + 1

        return map_s==map_t        