import sys
input = sys.stdin.readline
l = input().rstrip().split(' ')
ans = 0
for v in l:
    if v != '': ans += 1
print(ans)
