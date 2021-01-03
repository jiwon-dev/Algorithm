import sys
input=sys.stdin.readline
# 04m
for _ in range(int(input())):
    hp,mp,atk,de,a,b,c,d=map(int,input().split())
    hp+=a;mp+=b;atk+=c;de+=d
    if hp<1: hp=1
    if mp<1: mp=1
    if atk<0: atk=0
    print(hp+5*mp+2*atk+2*de)
