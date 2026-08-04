# brute force method

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0

        if len(height) == 1:
            return 0

        for i in range(len(height)):
            for j in range(i, len(height)):
                curr_area = (j-i) * min(height[i], height[j])
                if curr_area > area:
                    area = curr_area

        return area


# time-complexity: O(n^2)
# space-complexity: O(1)

# Optimal Solution

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = 0

        if n == 1:
            return 0

        l = 0
        r = n - 1

        while l < r:
            curr_area = (r-l) * min(height[l], height[r])

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            area = max(curr_area, area)

        return area


# time-complexity: O(n)
# space-complexity: O(1)
