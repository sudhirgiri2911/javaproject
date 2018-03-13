#!/bin/python3



if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    # Write Your Code Here
    rank={}
    prev=scores[0]
    rank[prev]=1
    count=2
    for i in range(1,len(scores)):
        curr=scores[i]
        if curr<prev:
            rank[curr]=count
            count+=1 
    for score in alice:
        flag=0
        for key,value in rank.items():
            if key<=score:
                print(value)
                flag=1
                break
        if flag!=1:
            print(len(rank)+1)
            