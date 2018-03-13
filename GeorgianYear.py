'''
Created on Nov 19, 2017

@author: Satyam
'''
def solve(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    return False


year = int(input().strip())
result = solve(year)
print(result)