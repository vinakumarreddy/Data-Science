def majorityelement(arr):
    frequency = {}
    arr1 = []
    n=len(arr)/3
    for i in arr:
        if  i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    for i in frequency:
        if frequency[i]>n:
            arr1.append(i)
            arr1.sort()
    return arr1
arr1=[1,2,3,4,1,2,1,2]
print(majorityelement(arr1))
