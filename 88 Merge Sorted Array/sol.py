class Solution:
    def merge(self, nums1, m, nums2, n: int):
        nums2.reverse()
        for i in range(len(nums1)):
            if len(nums2) and len(nums1) - i > len(nums2):
                if nums1[i] >= nums2[-1]:
                    for j in range(len(nums1)-1, i, -1):
                        nums1[j] = nums1[j-1]
                    nums1[i] = nums2.pop()
            else:
                if len(nums2):
                    nums1[i] = nums2.pop()
            
        print(nums1)
                
        