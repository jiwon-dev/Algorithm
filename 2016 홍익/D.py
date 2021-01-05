import sys
import os
n = 2**22
a = bytearray(n)
m = 8
unstdin = os.fdopen(sys.stdin.fileno(), 'rb', 1000000)
while True:
    try:
        b = 0
        while True:
            ch = unstdin.read(1)
            if b'0' <= ch <= b'9':
                b = 10*b+int(ch)
            elif ch == b' ':
                break
            else:
                raise EOFError
    except EOFError:
        break
    y, x = divmod(b, m)
    # int가 32비트이므로 하나의 int값(몫)에 32개의 수를 체크할 수 있는 공간을 만들 수 있음
    # 이 코드는 char형이므로 8로 나눔
    # a[몫]&(1<<나머지)으로 확인
    if not a[y] & (1<<x):
        print(b, end = ' ')
    a[y] |= (1<<x)
if b:
    y, x = divmod(b, m)
    if not a[y] & (1<<x):
        print(b, end = '')
