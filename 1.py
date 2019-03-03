class Solution:
    def twoSum(self, nums, target):
        time = 0

        for time in range(0, len(nums)):
            for j in range(time, len(nums)):
                if j == time:
                    continue
                if nums[time] + nums[j] == target:
                    return [time, j]
                continue


a = Solution()
nums = [2, 7, 11, 15]
print(a.twoSum(nums, 9))