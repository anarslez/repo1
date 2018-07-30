#1
for count in range(0,150):
    print(count)
#2
count = 200001
i = 1
for i in range(count):
        print(i*5)
#3
i = 1
for i in range(101):
    if i%5 == 0 and i%10 == 0:
        print('Dojo')
    elif i%5 == 0:
        print('Coding')
    else:
        print(i)
#4
i = 1
sum = 0
while i<500000:
    i = i+2
    sum = sum+i

print(sum)
#5
i = 2018
while i>4:
    i = i-4
    print(i)
#6
mult = 3
lownum = 2
highnum = 9
i = 1
for i in range(highnum):
    out = mult*i
    if out > lownum-1 and out < highnum+1:
        print(out)


