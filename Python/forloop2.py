#1
def bs(arr):
    for i in arr:
        if i>0:
            i = 'big'
        
    return arr

#2
def cp(arr):
    count = 0
    for i in arr:
        if i>0:
            count = count+1
    
    arr[len(arr)-1] = count
    return arr

#3
def sar(arr):
    sum = 0
    for i in arr:
        sum = sum+i
    
    return sum

#4
def avg(arr):
    av = 0
    for i in arr:
        av = av+i
    
    return av/len(arr)

#5
def le(arr):
    return len(arr)

#6
def mi(arr):
    min = arr[0]
    for i in arr:
        if min>i:
            min = i
        
    return min

#7
def ma(arr):
    max = arr[0]
    for i in arr:
        if max<i:
            max = i
        
    return max

#8
def ult(arr):
    max = arr[0]
    min = arr[0]
    avg = 0
    for i in arr:
        avg = avg+i
        if max<i:
            max = i
        if min>i:
            min = i
    
    ind = {"sumtotal":avg, "min":min, "max":max, "avg":avg/len(arr),"length":len(arr)}
    return ind

#9
def rev(arr):
    tmp = []
    for i in arr:
        tmp.append(i)
        arr[len(arr)-1-i]=tmp[i]
    
    return arr