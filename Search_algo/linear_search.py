def linear(a,num):
    for i in range(len(a)): 
        if a[i] == num: # checking searching element with every element of the array
            return "Element Found at position: {}".format(a.index(a[i]))
    return "Not Found"

#Time Complexcity :- O(n)
