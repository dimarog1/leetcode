import heapq
from typing import List


class Solution:
    def manh(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = {i: [] for i in range(n)}
        for i in range(n):
            p1 = points[i]
            for j in range(i + 1, n):
                p2 = points[j]
                dist = self.manh(p1, p2)
                graph[i].append([dist, j])
                graph[j].append([dist, i])

        res = 0
        visited = set()
        min_heap = [[0, 0]]
        while len(visited) != n:
            cost, p = heapq.heappop(min_heap)
            if p in visited:
                continue
            res += cost
            visited.add(p)
            for cost, tmp_p in graph[p]:
                if tmp_p not in visited:
                    heapq.heappush(min_heap, [cost, tmp_p])

        return res
