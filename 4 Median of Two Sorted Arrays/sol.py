class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if all([not nums1, not nums2]):
            return 0
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) % 2:
            return nums3[len(nums3) // 2]
        else:
            res = (nums3[len(nums3) // 2] + nums3[len(nums3) // 2 - 1]) / 2
            return res


s = Solution()
res = s.findMedianSortedArrays([1, 2], [3, 4])
print(res)