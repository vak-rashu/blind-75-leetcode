class Solution:
    def __init__(self):
        self.pair = []

    def check_pair(self, bday_list):
        for i in range(len(bday_list)):
            for j in range(i+1, len(bday_list)):

                if bday_list[j] == bday_list[i]:
                    self.pair.extend([bday_list[i], bday_list[j]])

        return self.pair


a = Solution()
b_l = [1, 2, 11, 1, 3, 4, 15, 4, 2, 5, 5, 15]
print(a.check_pair(b_l))
