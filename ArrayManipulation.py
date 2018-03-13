n, inputs = [int(n) for n in input().split(" ")]
list1 = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    list1[x-1] += incr
    if((y)<=len(list1)): list1[y] -= incr;
max1 = x = 0
for i in list1:
    x=x+i;
    if(max1<x): max1=x;
print(max1)