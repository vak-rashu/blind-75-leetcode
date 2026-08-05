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


# correct approach
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        val = []
        nums.sort()

        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r-=1
                elif three_sum < 0:
                    l+=1
                else:
                    val.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return val

# time-complexity: O(n^2)
# space-complexity: O(1)