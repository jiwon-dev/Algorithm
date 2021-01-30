import sys
input=sys.stdin.readline
# 14m
N=int(input())
dic={}
for _ in range(N):
    s=input().rstrip()
    if s in dic: dic[s]+=1
    else: dic[s]=1

items=sorted(dic.items(),key=lambda x:float(x[0]))
cnt,idx=0,0
while True:
    for i in range(items[idx][1]):
        cnt+=1
        print(items[idx][0])
        if cnt==7: sys.exit()
    idx+=1
    
