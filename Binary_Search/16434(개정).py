import sys
input=sys.stdin.readline
n,atk=map(int,input().split())
room=[tuple(map(int,input().split())) for _ in range(n)]

def paramin(F,l,r):
    while l<=r:
        mid=(l+r)//2
        if F(mid): ans,r=mid,mid-1
        else: l=mid+1
    return ans

def pwn(maxhp):
    h=maxhp; a=atk
    for t,ai,hi in room:
        if t==1:
            h-=ai*(hi//a-(hi%a==0))
            if h<=0: return False
        else: a+=ai; h=min(maxhp,h+hi)
    return True

print(paramin(pwn,1,10**18))
