from math import sqrt

class Solution:
    def prime_number(self, num: int) -> bool:

        l = []
        # for i in range(1, int(sqrt(num)+1.0)):

        #     if num % i == 0 :
        #         m = num // i
        #         l.extend([i, m])

        # if len(l) > 2:
        #     return False
        # else:
        #     return True

        i = 1
        while i*i <= num:
            if num % i == 0:
                m = num // i
                l.extend([i, m])

            i+=1
        
        if len(l) > 2:
            return False
        else:
            return True

a = Solution()
args = eval(input("Enter your value(q to quit): "))
while args != "q":
    print(a.prime_number(args))
    args = eval(input("Enter your value(q to quit): "))
