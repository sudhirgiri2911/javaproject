a = input()
b = [i for i in range(int(a))]

c = sum(b)
max1=0
min1=99999999
for i in b:
    if c-i > max1:
        max1 = c-i
    if c-i < min1:
        min1 = c-i
print(min1,max1)
    