'''
Created on Nov 19, 2017

@author: Satyam
'''
def solve(n, s, d, m):
    # Complete this function
    count=0
    for i in range(n-m+1):
        print(s[i:i+m])
        if sum(s[i:(i+m-1)])==d:
            count+=1
    return count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)