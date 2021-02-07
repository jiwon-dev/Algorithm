import sys
input=sys.stdin.readline
# 5m
x=int(input())
prev=0
while True:
    x=int(str(x)[0])*len(str(x))
    if prev==x:
        print('FA')
        sys.exit()
    prev=x
print('NFA')
