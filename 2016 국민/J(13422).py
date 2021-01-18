import sys
input=sys.stdin.readline
# 1h 41m (2)
for _ in range(int(input())):
    N,M,K=map(int,input().split())
    H=list(map(int,input().split()))
    for j in range(M-1): H.append(H[j])
    for i in range(1,N+M-1): H[i]=H[i-1]+H[i]
    
    ans=0
    H=[0]+H
    for i in range(M,N+M):
        if H[i]-H[i-M]<K: ans+=1

    if N==M:
        if H[M]<K: print(1)
        else: print(0)
    else: print(ans)
