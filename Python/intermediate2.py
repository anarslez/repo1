#1a
x[1][0]=15
#1b
students[0]['last_name']='Bryant'
#1c
sports_directory['soccer'][0]='andres'
#1d
z[0]['y']=30
#2
def loop(arr):
    for i in arr:
        for key, val in i.items():
            print(key, " = ", val)

#3
def loop(arr,kay):
    for i in arr:
        for key, val in i.items():
            if key == kay:
                print(val)   

#4
def loop(arr):
    for key, val in dojo.items():
        print(len(key)-2)
        print(key)
        for i in val:
            print(i)
