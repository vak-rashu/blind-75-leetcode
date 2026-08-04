#brute force method

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

