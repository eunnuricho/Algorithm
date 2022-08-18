import sys

input = sys.stdin.readline

N, M = map(int, input().split())

_dict = {}

for i in range(N):
    pkm = input().rstrip()
    _dict[pkm] = (i + 1)
    _dict[i + 1] = pkm

for j in range(M):
    qna = input().rstrip()
    if qna.isdigit():
        print(_dict[int(qna)])
    else:
        print(_dict[qna])