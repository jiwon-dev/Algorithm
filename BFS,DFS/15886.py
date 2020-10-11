import sys
input=sys.stdin.readline
# 15m 16s
# 'EW'의 개수가 정답인데 dfs로 하면 사이클의 개수가 정답
n=int(input())
print(input().rstrip().count('EW'))
