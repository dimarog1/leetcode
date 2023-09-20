class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        if len(nums) < 2 or k < 1:
            return

        i, j = 0, len(nums) - k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i, j = len(nums) - k, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        nums.reverse()


# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         k = k % len(nums)
#         if len(nums) < 2 or k < 1:
#             return
#
#         for i in range((len(nums) - k) // 2):
#             nums[i], nums[len(nums) - k - i - 1] = nums[len(nums) - k - i - 1], nums[i]
#
#         for i in range(k // 2):
#             nums[len(nums) - k + i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[len(nums) - k + i]
#
#         nums.reverse()
