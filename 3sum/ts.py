class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        set_res = set()
        nums.sort()
        for i in range(len(nums)):
            left_maker = i + 1
            right_marker = len(nums) - 1
            while left_maker < right_marker:
                temp_sum = nums[i] + nums[left_maker] + nums[right_marker]
                if temp_sum == 0:
                    set_res.add((nums[i], nums[left_maker], nums[right_marker]))
                    left_maker += 1
                    right_marker -= 1
                elif temp_sum < 0:
                    left_maker += 1
                else:
                    right_marker -= 1
        res = [list(item) for item in set_res]
        res.sort()
        return res


def main():
    s = Solution()
    print(s.threeSum([18, -16, 9, 12, 18, -18, -5, 11, 13, -1, -8, -16, 15, 13, 2, -14, -3, 5]))

    #[[-18, 5, 13], [-16, 5, 11], [-14, -1, 15], [-14, 2, 12], [-14, 5, 9], [-8, -5, 13], [-8, -3, 11], [-8, -1, 9]]
    #[[-18, 5, 13], [-16, 5, 11], [-14, -1, 15], [-14, 2, 12], [-14, 5, 9], [-8, -5, 13], [-8, -3, 11], [-8, -1, 9]]

if __name__ == '__main__':
    main()

