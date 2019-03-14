# very simple
def bubble(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j] < arr[i]: 
                arr[j],arr[i] = arr[i],arr[j]
            print('step {}: {}'.format(i+j,arr))
    return arr
arr2 = [5,7,3,8,2,1]
bubble(arr2)
