def remove_dulpicate(arr):
    if (len(arr))==0:
        return 0
    j=1
    for i in range(len(arr)):
        if arr[i] != arr[j]:
            j+=1
            arr[j]=arr[i]

    return j+1
# use case
arr = [1,2,3,3,4,5,6,6,6,7]
remove_duplicate(arr)
print(arr)