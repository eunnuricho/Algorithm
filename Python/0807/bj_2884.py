hour, minute = map(int, input().split())

if minute >= 45:
    print(hour, (minute - 45), sep=' ')

else:
    if hour == 0:
        print(23, (minute + 15), sep=' ')
    else:
        print((hour - 1), (minute + 15), sep=' ')