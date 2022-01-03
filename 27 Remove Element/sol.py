class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occurrences = 0
        for num in nums:
            if num == val:
                occurrences += 1
        shift = occurrences
        num_len = len(nums) - occurrences
        for i in range(len(nums)-occurrences):
            if nums[i] == val:
                while nums[i] == nums[-shift]:
                    shift -= 1
                nums[i], nums[-shift] = nums[-shift], nums[i]
                shift -= 1
        return len(nums) - occurrences
