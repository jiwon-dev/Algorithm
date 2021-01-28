import sys
input=sys.stdin.readline
# 04m
def solve(depth,total,s):
    global ans
    if depth==N:
        if s[0]=='0': return
        if total%3==0: ans+=1
        return

    for v in [0,1,2]:
        solve(depth+1,total+v,s+str(v))

N=int(input())
ans=0
solve(0,0,"")
print(ans)
        
