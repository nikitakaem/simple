
#Linear functions:

#1
def search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i    #or return True #or return A[i] - its name of key
    return None         #or return False

x1 = [2, 5, 6, 7, 8, 8, 10]

print ("L1")
print (search(x1, 8))

#2
def search2(A, key):
    i = 0
    while i < len(A) and A[i] != key: #check all list #A[i] - index number
        i += 1
    return i < len(A) #if i < len(A) - its in list so = true

x2 = [2, 5, 6, 7, 8, 8, 10]

print ("L2")
print (search2(x2, 10))


#2v2
def search2v2(A, key):
    i = 0
    while i < len(A) and A[i] != key: #A[i] - format to index#, not #in list
        i += 1
    if i < len(A):
        return i    #istead if i in list (coz its <len(A)) return i
    else:
        return None

x2v2 = [2, 5, 6, 7, 8, 8, 10]

print ("L2v2")
print (search2v2(x2v2, 4))

#bilinear functions:

#1
def bsearch(A, key):
    low = 0                 
    high = len(A) - 1   #why -1?????
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == key:
            return mid
        if A[mid] > key:    
            high = mid -1 
        else:
            low = mid +1
    return None

ml = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print ("B1")
print (bsearch(ml, 14))

def bsearch2(A, key): 
    left = -1 
    right = len(A) 
    while right > left + 1: 
        middle = (left + right) // 2 
        if A[middle] > key: 
            right = middle 
        else: 
            left = middle 
    return right

ml2 = [1, 3, 5, 6, "t"]
print ("B2")
print (bsearch2(ml2, 3))

def bsearch3(A, k): 
    low = 0
    high = len(A) - 1
    while high > low + 1: 
        mid = (low + high) // 2 
        if A[mid] >= k: 
            hight = mid
        else: 
            low = mid
    return high

ml3 = [1, 3, 5, 6, "t"]
print ("B3")
print (bsearch3(ml3, 2))



