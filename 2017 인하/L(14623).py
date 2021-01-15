import sys
input=sys.stdin.readline
# 01h 08m
B1=int('0b'+input().rstrip(),2)
B2=int('0b'+input().rstrip(),2)
print(bin(B1*B2)[2:])
