# def two_pointers(array):
#     l, r = 0, len(array)-1

#     while l!=r:
#         print(array[l])
#         l+=1
#         print(array[r])
#         r-=1
#         if l == r:
#             print(array[l])

# def two_sum_two_pointers(array, target):
#     l, r = 0, len(array)-1

#     while l!=r:
#         target_sum = array[l] + array[r]
#         if target_sum == target:
#             return ([l, r], [array[l], array[r]])
#         elif target_sum > target:
#             r-=1
#         else:
#             l+=1

def two_pointers_merge_sorted_list(array1, array2):
    l, r = 0, 0
    n, m = len(array1), len(array2)
    merged_array = []
    min_val = 0

    while True:
        min_val = min(array1[l], array2[r])
        merged_array.append(min_val)

        if min_val == array1[l]:
            l+=1
        else:
            r +=1

        # if r == m:
        #     merged_array.extend(array1[l:])
        #     break

        if r == m:
            merged_array.extend(array1[l:])
            break
        if l == n:
            merged_array.extend(array2[r:])
            break

    return merged_array


# def two_pointers_merge_sorted_list(array1, array2):

#     l, r = 0, 0
#     merged_list = []    
#     # we might remain with some elements
#     while True:
#         min_val = min(array1[l], array2[r])
#         merged_list.append(min_val)

#         if min_val == array1[l]:
#             l+=1
#         else:
#             r +=1

#         if l == len(array1)-1:
#             merged_list.extend(array2[r:])
#             break
#         else:
#             merged_list.extend(array1[l:])
#             break

#     return merged_list

array1 = [1, 3, 4]
array2 = [-1, 0, 2]
print(two_pointers_merge_sorted_list(array1, array2))
