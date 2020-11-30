import sys
import copy
input=sys.stdin.readline
# 43m 45s
def solve(x,y,n):
    global grid
    if n==1:
        print(grid[0][0])
        return
    key=[[] for _ in range(n//2)]
    idx=0
    for i in range(x,x+n,2):
        for j in range(y,y+n,2):
            sam=[]
            for k in range(i,i+2):
                for l in range(j,j+2):
                    sam.append(grid[k][l])
            sam.sort()
            key[idx].append(sam[2])
        idx+=1
    grid=copy.deepcopy(key)
    solve(x,y,n//2)
N=int(input())
grid=[list(map(int,input().split())) for _ in range(N)]
solve(0,0,N)
