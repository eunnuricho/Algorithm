N = int(input())

_six = 666
cnt = 0

while True:
    _target = str(_six)
    if '666' in _target:
        cnt += 1

    if cnt == N:
        print(_target)
        break

    _six += 1