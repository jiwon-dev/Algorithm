import sys
input=sys.stdin.readline
# 03m
a,b,c,d,e,f=int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
one=[a,b,c,d]
two=[e,f]
one.sort(reverse=True)
two.sort(reverse=True)
print(sum(one[:3])+sum(two[:1]))
