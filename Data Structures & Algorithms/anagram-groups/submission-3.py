class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        get_pos = lambda char: ord(char) - 97
        get_char = lambda idx: chr(idx+97)
        
        def convert_to_string(map_arr):
            l = len(map_arr)
            result = ''
            for i in range(l):
                if map_arr[i] != 0:
                    result += get_char(i) + str(map_arr[i])
            return result

        
        hash_map = {}
        for strings in strs:
            map_arr = [0]*26
            for i in strings:
                map_arr[get_pos(i)] += 1
            converted = convert_to_string(map_arr)
            hash_map[converted] = hash_map.get(converted, []) + [strings]

        result = []
        for values in hash_map.values():
            result.append(values)

        return result

