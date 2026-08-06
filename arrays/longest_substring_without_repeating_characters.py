class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subseq = []

        for i in range(len(s)):
            # print(s[i])
            if s[i] in subseq:
                subseq = []
            subseq.append(s[i])
            # print(subseq)

        return len(subseq)

a = Solution()
print(a.lengthOfLongestSubstring("pwwkew"))
