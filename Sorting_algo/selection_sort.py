def selection(arr):
    for i in range(len(arr)):
        #print('i: ',i) to clear the confusion
        imin = i
        p = i+1
        for j in range(p,len(arr)):
            if arr[j] < arr[imin]:
                imin = j
            #print('j: ',j)
        arr[i],arr[imin] = arr[imin],arr[i]
        
    return arr

#Time complexcity for best and worst case is: O(n^2)

'''def selection(arr):
    limit = len(arr)
    for i in range(limit):
        for j in range(i,limit):
            if arr[j] < arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr'''


