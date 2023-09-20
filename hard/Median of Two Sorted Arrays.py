from typing import List


class Solution:
    def merge(self, nums1, nums2):
        if len(nums1) == 0:
            return nums2
        if len(nums2) == 0:
            return nums1
        res = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] >= nums2[j]:
                res.append(nums2[j])
                j += 1
            elif nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
        res.extend(nums1[i:] if i < len(nums1) else [])
        res.extend(nums2[j:] if j < len(nums2) else [])

        return res

    def median(self, nums):
        if len(nums) < 1:
            return 0
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
        return nums[len(nums) // 2]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = self.merge(nums1, nums2)
        return self.median(a)


s = Solution()
print(s.findMedianSortedArrays([1, 2], [3, 4]))
