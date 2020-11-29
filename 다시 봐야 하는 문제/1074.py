import sys

result = 0


def z(n, x, y):
    global result
    if x == r and y == c:
        print(int(result))
        exit(0)

    if n == 1:
        # 한 칸씩 돌면서 좌표를 찾아가며 방문 횟수를 누적
        result += 1
        return

    if not (x <= r < x + n and y <= c < y + n):
        # r,c가 위치한 사분면에 벗어나는 곳에 있으면 총 사각형 수 만큼 방문 횟수에 누적 후 사각형 안을 살펴볼 필요 없으므로 return
        result += n * n
        return
    z(n / 2, x, y)
    z(n / 2, x, y + n / 2)
    z(n / 2, x + n / 2, y)
    z(n / 2, x + n / 2, y + n / 2)


n, r, c = map(int, sys.stdin.readline().split(' '))
z(2 ** n, 0, 0)
