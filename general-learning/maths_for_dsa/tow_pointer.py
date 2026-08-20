def two_pointers(array):
    l, r = 0, len(array)-1

    while l<=r:
        print(array[l])
        l+=1
        print(array[r])
        r-=1


array = [1, 2, 3, 4, 5]
two_pointers(array=array)
