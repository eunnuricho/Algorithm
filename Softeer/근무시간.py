import sys

shift = 0

for _ in range(5):
    a, b = sys.stdin.readline().split()

    tmp1 = list(a)
    tmp2 = list(b)

    del tmp1[2]
    del tmp2[2]

    hour_in = int(''.join(tmp1[:2]))
    hour_out = int(''.join(tmp2[:2]))

    minute_in = int(''.join(tmp1[2:]))
    minute_out = int(''.join(tmp2[2:]))

    shift += ((hour_out - hour_in) * 60) + (minute_out - minute_in)

print(shift)