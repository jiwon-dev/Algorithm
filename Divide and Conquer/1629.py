import sys
input=sys.stdin.readline
A,B,C=map(int,input().split())
def POW(A,B,C):
    if B==1: return A%C
    val=POW(A,B//2,C)
    val=val*val%C
    if B%2==0: return val
    return val*A%C
print(POW(A,B,C))
