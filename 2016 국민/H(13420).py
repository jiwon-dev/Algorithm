import sys
input=sys.stdin.readline
# 47m
for _ in range(int(input())):
    s=input().split()
    p1,ex,p2=int(s[0]),s[1],int(s[2])
    ans='wrong answer'
    if ex=='+' and p1+p2==int(s[-1]): ans='correct'
    if ex=='-' and p1-p2==int(s[-1]): ans='correct'
    if ex=='*' and p1*p2==int(s[-1]): ans='correct'
    if ex=='/' and p1//p2==int(s[-1]): ans='correct'
    print(ans)
