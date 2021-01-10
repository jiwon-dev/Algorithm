import sys
input=sys.stdin.readline
def solve(depth,res):
    if depth==N:

        print(res)
        return

    if depth==0:
        for v in [2,3,5,7]: solve(depth+1,v)
    else:
        for v in [1,3,5,7,9]:
            temp=res*10+v
            if temp%3==0: continue
            if temp%5==0: continue
            if temp%7==0: continue
            solve(depth+1,res*10+v)
            
N=int(input())
solve(0,0)

