def secondlargest(arr):
    largest=float("-inf")
    secondlargest=float("-inf")
    for i in range(len(arr)-1):
        if arr[i]>largest:
            largest=arr[i]
            secondlargest=largest
        elif arr[i]>secondlargest and arr[i]!=largest:
            secondlargest=arr[i]
    return secondlargest
arr = [1,2,3,4,5,6]
print(secondlargest(arr))
