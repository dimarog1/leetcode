from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        flag = True
        while fast != slow or flag:
            flag = False
            fast = nums[nums[fast]]
            slow = nums[slow]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


s = Solution()
a = [4, 7, 3, 2, 1, 6, 7, 5]
print(s.findDuplicate(a))
