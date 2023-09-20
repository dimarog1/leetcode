from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = dict()
        res = []
        for i in range(len(groupSizes)):
            elem = groupSizes[i]
            if elem not in d:
                d[elem] = [i]
            else:
                if len(d[elem]) < elem:
                    d[elem].append(i)
                else:
                    res.append(d[elem])
                    d[elem] = [i]
        for elem in d:
            if d[elem] not in res:
                res.append(d[elem])

        return res
