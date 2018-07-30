#1
def cd(num):
    arr = []
    for i in range(num,-1,-1):
        arr.append(i)
    
    return arr

#2
def pr(p,r):
    pirnt(p)
    return r

#3
def fpl(arr):
    return len(arr)+arr[0]

#4
def gts(arr):
    newarr = []
    if len(arr)==1:
        return false
    for i in arr:
        if i > arr[1]:
            newarr.append(i)
    
    return newarr

#5
def tltv(l,v):
    arr = []
    for i in range(l):
        arr.apend(v)

    return arr