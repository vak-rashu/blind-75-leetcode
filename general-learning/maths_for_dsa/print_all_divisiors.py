from math import sqrt

class Solution:
    def print_all_divisiors(self, num:int) -> List[int]:

        l = []

        for i in range(1, int(sqrt(num) + 1.0)):
            if num % i == 0:
                m = num // i
                if (m != i):
                    l.extend([i, m])
                else:
                    l.append(i)
        l.sort()

        return l

a = Solution()
args = eval(input("Enter your value(q to quit): "))
while args != "q":
    print(a.print_all_divisiors(args))
    args = eval(input("Enter your value(q to quit): "))
