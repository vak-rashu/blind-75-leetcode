# my-approach: Brute Force
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        val = []
        for i in range(len(nums)):
            if i < -2:
                break
            val1 = []
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        val1 = [nums[i], nums[j], nums[k]]
                        val.append(val1)

            return val

# time-complexity: O(n^3)
# space-complexity: O(n)
