class Solution:
    def fibonacci(self, n):

        count = 0
        i, j = 0, 1
        while count < n:

            print(i)
            i, j = j, i + j

            count +=1

        # for i in range(n):
        #     if i == 0:
        #         fibonacci_sum.append(0)
        #     elif i == 1:
        #         fibonacci_sum.append(1)
        #     else:
        #         curr_sum = fibonacci_sum[i-1]+fibonacci_sum[i-2]
        #         fibonacci_sum.append(curr_sum)

        # return fibonacci_sum

a = Solution()
a.fibonacci(11)
# args = eval(input("Enter your value(q to quit): "))
# while args != "q":
#     a.fibonacci(args)
#     args = eval(input("Enter your value(q to quit): "))
