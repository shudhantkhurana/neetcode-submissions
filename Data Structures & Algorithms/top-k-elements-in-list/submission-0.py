class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in nums:
            hash_map[i] = hash_map.get(i,0) + 1

        arr = []
        while k != 0:
            max_key = max(hash_map, key=hash_map.get)
            print(max_key)
            arr.append(max_key)
            hash_map[max_key] = -2000
            k -= 1 
        return arr