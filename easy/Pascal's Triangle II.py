from math import factorial
from typing import List


class Solution:
    def c(self, n: int, k: int) -> int:
        n, k = max(n, k), min(n, k)
        return factorial(n) // (factorial(k) * factorial(n - k))

    def generate(self, numRows: int) -> List[List[int]]:
        res = [[] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(i + 1):
                res[i].append(self.c(i, i - j))
        return res
