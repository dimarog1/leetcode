class Solution:
    def minDeletions(self, s: str) -> int:
        d = dict()
        for elem in s:
            if elem not in d:
                d[elem] = 1
            else:
                d[elem] += 1

        res = 0
        used = set()
        for elem in sorted(d.values(), reverse=True):
            while elem > 0:
                if elem not in used:
                    used.add(elem)
                    break
                elem -= 1
                res += 1

        return res
