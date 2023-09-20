from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {0: 1}
        s = 0
        res = 0
        for num in nums:
            s += num
            if s - k in hash_map:
                res += hash_map[s - k]
            if s not in hash_map:
                hash_map[s] = 1
            else:
                hash_map[s] += 1
        return res
