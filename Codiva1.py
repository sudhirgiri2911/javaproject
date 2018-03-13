#!/bin/python3

#import sys

def check_prime(num):
    
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False

    return True


def maxDifference(startVal, endVal):
    # Complete this function
    flag=0
    temp1=temp2=0
    for i in range(startVal,endVal+1):
        if check_prime(i):
            if flag==0:
                flag=1
                temp1=i
            else:
                temp2=i
    if temp1==0 or temp2==0:
        return 0
    return temp2-temp1
            


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        startVal, endVal = input().strip().split(' ')
        startVal, endVal = [int(startVal), int(endVal)]
        result = maxDifference(startVal, endVal)
        print(result)
