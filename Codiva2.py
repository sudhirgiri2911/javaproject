#!/bin/python3

def k_price(n,brands,prices,d,cameras,k):
    price_of_camera=[]
    for i in cameras:
        for j in range(n):
            if i==brands[j]:
                price_of_camera.append(prices[j])
    length_of_price=len(price_of_camera)
    if length_of_price==0 or length_of_price<k:
        return -1
    price_of_camera.sort()
    return price_of_camera[k-1]
    
    
if __name__ == "__main__":
    n = int(input().strip())
    brands = list(map(int, input().strip().split(' ')))
    prices = list(map(int, input().strip().split(' ')))
    q = int(input().strip())
    for a0 in range(q):
        d = int(input().strip())
        cameras = list(map(int, input().strip().split(' ')))
        k = int(input().strip())
        print(k_price(n,brands,prices,d,cameras,k))
