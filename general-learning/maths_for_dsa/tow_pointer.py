# def two_pointers(array, target):
#     target_sum = 0
#     l, r = 0, len(array)-1

#     while l!=r:
#         print(array[l])
#         l+=1
#         print(array[r])
#         r-=1

def two_sum_two_pointers(array, target):
    l, r = 0, len(array)-1

    while l!=r:
        target_sum = array[l] + array[r]
        if target_sum == target:
            return ([l, r], [array[l], array[r]])
        elif target_sum > target:
            r-=1
        else:
            l+=1


array = [11, 4, 3, 2, 5]
target = 6
print(two_sum_two_pointers(array=array, target=target))
