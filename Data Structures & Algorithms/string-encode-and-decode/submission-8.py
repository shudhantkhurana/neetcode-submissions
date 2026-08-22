class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return 'xx00xx'
        if len(strs) == 1:
            return strs[0]
        result = "shudhant".join(strs)
        return result

    def decode(self, s: str) -> List[str]:
        if s == 'xx00xx':
            return []
        if s == '':
            return ['']
        if 'shudhant' in s:
            result = s.split("shudhant")
            print(result, len(result))
            return result
        else:
            return [s]