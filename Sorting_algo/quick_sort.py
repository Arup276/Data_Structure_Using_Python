def quick(arr):
    start = 0
    end = len(arr)-1
    #print(start,end,arr)
    quicksort(arr,start,end)
    
    
def quicksort(arr,start,end):
    if start < end:
        pindex = partition(arr,start,end)
        print(pindex)
        quicksort(arr,start,pindex-1)
        quicksort(arr,pindex+1,end)
        
def partition(arr,start,end):
    end_ind = end
    pivot = arr[end]
    pindex = start
    for i in range(start,end):
        if arr[i] <= pivot:
            arr[i],arr[pindex]=arr[pindex],arr[i]
            pindex += 1
            
    arr[end_ind],arr[pindex] = arr[pindex],arr[end_ind] # pivot,arr[pindex] = arr[pindex],pivot ---this is not work because last position is not changing
    print(arr)
    #print('A: pindex',pindex)
    return pindex


# Time complexity
# Best case,average case : O(nlogn)
# Worst case : O(n^2)

# Best thing about quick sort is it's inplace sorting algoritham and space complexity is : O(1) , no extra memory needed.
