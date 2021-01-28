import sys
# 01h 02m
n=int(input())
count=0
max_value=0
array=[0 for _ in range(100001)]
pan=list(map(int,input().split()))
for i in range(2*n):
    if array[pan[i]]!=0:
        count-=1
    else:
        array[pan[i]]+=1
        count+=1
    if max_value<count:
        max_value=count
print(max_value)
