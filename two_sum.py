# two sum

# brute force method
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# time-complexity: O(n^2)

# HashMap method
class TwoSum:

    def sol(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            y = target - nums[i]
            if y in hashmap:
                return [i, hashmap[y]]
            hashmap[nums[i]] = i

# time-complexity: O(n)
# trade-off: space-complexity: O(n)