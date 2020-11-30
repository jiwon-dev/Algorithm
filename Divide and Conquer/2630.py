import sys
input=sys.stdin.readline
# 18m 12s
def solve(x,y,n):
    global a,b
    for i in range(x,x+n):
        for j in range(y,y+n):
            if grid[x][y]!=grid[i][j]:
                solve(x,y,n//2)
                # 1사분면
                solve(x,y+n//2,n//2)
                # 2사분면
                solve(x+n//2,y,n//2)
                # 3사분면
                solve(x+n//2,y+n//2,n//2)
                # 4사분면
                return
            
    if grid[x][y]: b+=1
    else: a+=1

N=int(input())
a,b=0,0
grid=[list(map(int,input().split())) for _ in range(N)]
solve(0,0,N)
print(a)
print(b)
    
