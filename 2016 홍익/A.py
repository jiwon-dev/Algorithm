import sys
input=sys.stdin.readline
# 05m
dic={'A':(0,1),'B':(0,2),'C':(0,3),'D':(1,2),'E':(1,3),'F':(2,3)}
S=input().rstrip()
cup=[0]*4
cup[0]=1;cup[3]=2

for x in S:
    a,b=dic[x]
    cup[a],cup[b]=cup[b],cup[a]
print(cup.index(1)+1)
print(cup.index(2)+1)
