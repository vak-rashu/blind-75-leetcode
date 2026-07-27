# contains duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for i in nums:
            if i in hashmap:
                return True
            hashmap.add(i)
        return False
# time complexity: O(n)
# space complexity: O(n)

#
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list.sort(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
